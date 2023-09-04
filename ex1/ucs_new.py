import heapq
from collections import defaultdict


def ucs(graph, start_node, goal_node):
    # Step 1: SET STATUS = 1 (ready state) for each node in G
    status = {node: 1 for node in graph}

    # Step 2: Initialize the cost dictionary with infinity for all nodes except the start node
    cost = {node: float('inf') for node in graph}
    cost[start_node] = 0

    # Step 3: Initialize the priority queue with the start node and its cost
    queue = [(0, start_node, [start_node])]  # (cost, node, path)

    while queue:
        # Step 4: Pop the node with the lowest cost from the priority queue
        current_cost, current_node, path = heapq.heappop(queue)

        # Step 5: Process the node and set its STATUS = 3 (processed state)
        print("Processing node:", current_node)
        status[current_node] = 3

        # Step 6: Check if the goal node is reached
        if current_node == goal_node:
            print("Goal node reached.")
            print("Cost of the node:", current_cost)
            print("Path:", " -> ".join(path))
            return

        # Step 7: Explore the neighbors of the current node
        for neighbor, edge_cost in graph[current_node].items():
            # Step 8: Calculate the new cost to reach the neighbor
            new_cost = current_cost + edge_cost

            # Step 9: If the new cost is lower than the current cost, update the cost and enqueue the neighbor
            if new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                heapq.heappush(queue, (new_cost, neighbor, path + [neighbor]))

                # Step 10: Set the neighbor's STATUS = 2 (waiting state) if it's not already processed
                if status[neighbor] != 3:
                    status[neighbor] = 2

    print("Goal node not reached.")
    print("Queue after UCS:", queue)
    print("Status after UCS:", status)


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


def delete_node(graph, node):
    if node in graph:
        del graph[node]
        for neighbor in graph:
            if node in graph[neighbor]:
                del graph[neighbor][node]
        print("Node deleted.")
    else:
        print("Node not found in the graph.")


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
        print("6. UCS")
        print("7. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_edge(graph)
            print(graph)
        elif choice == 2:
            add_node(graph)
            print(graph)
        elif choice == 3:
            delete_edge(graph)
            print(graph)
        elif choice == 4:
            node = input("Enter the node to delete: ")
            delete_node(graph, node)
            print(graph)
        elif choice == 5:
            graph, num_vertices = create_graph()
        elif choice == 6:
            if num_vertices == 0:
                print("Create the graph first.")
                continue
            start_node = input("Enter the start node for UCS: ")
            goal_node = input("Enter the goal node for UCS: ")
            ucs(graph, start_node, goal_node)
        elif choice == 7:
            break
        else:
            print("Invalid choice. Please try again.")
