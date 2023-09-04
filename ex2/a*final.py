from collections import defaultdict
from queue import PriorityQueue


def reconstruct_path(cameFrom, current):
    total_path = [current]
    while current in cameFrom.keys():
        current = cameFrom[current]
        total_path.insert(0, current)
    return total_path


def add_edge(graph):
    u, v, cost = input("Enter the edge to add (format: u v cost): ").split()
    graph[u][v] = int(cost)
    graph[v][u] = int(cost)


def add_node(graph):
    new_node = input("Enter the node to add: ")
    graph[new_node] = {}


def delete_edge(graph):
    u, v = input("Enter the edge to delete (format: u v): ").split()
    if v in graph[u]:
        del graph[u][v]
    if u in graph[v]:
        del graph[v][u]


def delete_node(graph):
    node_to_delete = input("Enter the node to delete: ")
    if node_to_delete in graph:
        del graph[node_to_delete]
        for node in graph:
            if node_to_delete in graph[node]:
                del graph[node][node_to_delete]


def create_graph():
    graph = defaultdict(dict)

    num_vertices = int(input("Enter the number of vertices: "))
    num_edges = int(input("Enter the number of edges: "))

    for i in range(num_edges):
        edge_input = input(f"Enter edge {i + 1} (format: u v cost): ")
        u, v, cost = edge_input.split()
        graph[u][v] = int(cost)
        graph[v][u] = int(cost)

    return graph, num_vertices


def A_Star(graph, start, goal, h):
    # The set of discovered nodes that may need to be (re-)expanded.
    # Initially, only the start node is known.
    openSet = PriorityQueue()

    # For node n, cameFrom[n] is the node immediately preceding it on the cheapest path from the start
    # to n currently known.
    cameFrom = {}

    # For node n, gScore[n] is the cost of the cheapest path from start to n currently known.
    gScore = {node: float('inf') for node in graph}
    gScore[start] = 0

    # For node n, fScore[n] := gScore[n] + h(n). fScore[n] represents our current best guess as to
    # how cheap a path could be from start to finish if it goes through n.
    fScore = {node: float('inf') for node in graph}
    fScore[start] = h[start]

    openSet.put((fScore[start], start))

    while not openSet.empty():
        current = openSet.get()[1]

        # Check if current is the goal node
        if current == goal:
            path = reconstruct_path(cameFrom, current)
            cost = gScore[current]
            return path, cost

        for neighbor in graph[current]:
            tentative_gScore = gScore[current] + graph[current][neighbor]
            if tentative_gScore < gScore[neighbor]:
                cameFrom[neighbor] = current
                gScore[neighbor] = tentative_gScore
                fScore[neighbor] = gScore[neighbor] + h[neighbor]
                openSet.put((fScore[neighbor], neighbor))

    # Open set is empty but goal was never reached
    return "failure", float('inf')


def display_graph(graph):
    print("Graph:")
    for node, neighbors in graph.items():
        print(f"Node {node}:")
        for neighbor, cost in neighbors.items():
            print(f"  -> Neighbor: {neighbor}, Cost: {cost}")

if __name__ == "__main__":
    graph = defaultdict(dict)
    num_vertices = 0

    while True:
        print("\nMenu:")
        print("1. Add edge")
        print("2. Add node")
        print("3. Delete edge")
        print("4. Delete node")
        print("5. Create graph")
        print("6. Perform A* search")
        print("7. Display graph")
        print("8. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_edge(graph)
        elif choice == 2:
            add_node(graph)
        elif choice == 3:
            delete_edge(graph)
        elif choice == 4:
            delete_node(graph)
        elif choice == 5:
            graph, num_vertices = create_graph()
        elif choice == 6:
            if num_vertices == 0:
                print("Please create a graph first.")
                continue

            start_node = input("Enter the start node: ")
            goal_node = input("Enter the goal node: ")

            h = {}
            for node in graph:
                cost = input(f"Enter the heuristic cost for node {node}: ")
                h[node] = int(cost)

            path, cost = A_Star(graph, start_node, goal_node, h)
            if cost != float('inf'):
                print("Path:", path)
                print("Total Cost:", cost)
            else:
                print("No path found.")
        elif choice == 7:
            display_graph(graph)
        elif choice == 8:
            break
        else:
            print("Invalid choice. Please try again.")
