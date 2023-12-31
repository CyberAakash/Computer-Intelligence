import heapq

class Node:
    def __init__(self, data, heuristic):
        self.data = data
        self.neighbors = []
        self.heuristic = heuristic
        self.g_cost = float('inf')

    def __repr__(self):
        return f"Node({self.data})"

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_node(self, node, heuristic):
        self.vertices[node] = Node(node, heuristic)

    def add_edge(self, start, end, cost):
        node1 = self.vertices[start]
        node2 = self.vertices[end]
        node1.neighbors.append((end, cost))
        node2.neighbors.append((start, cost))

    def astar_search(self, start, destination):
        visited = set()
        pq = []
        heapq.heappush(pq, (0 + self.vertices[start].heuristic, 0, [start]))

        while pq:
            current_cost, g_cost, current_path = heapq.heappop(pq)
            current_vertex = current_path[-1]

            if current_vertex == destination:
                return current_cost, current_path

            if current_vertex in visited:
                continue

            visited.add(current_vertex)
            current_node = self.vertices[current_vertex]

            for neighbor, cost in current_node.neighbors:
                if neighbor in visited:
                    new_g_cost = g_cost + cost
                    if new_g_cost < self.vertices[neighbor].g_cost:
                        self.vertices[neighbor].g_cost = new_g_cost
                else:
                    new_g_cost = g_cost + cost
                    new_h_cost = self.vertices[neighbor].heuristic
                    new_cost = new_g_cost + new_h_cost
                    new_path = current_path + [neighbor]
                    heapq.heappush(pq, (new_cost, new_g_cost, new_path))

        return float('inf'), None

def main():
    graph = Graph()

    # Get the goal node from the user initially.
    goal_node = input("Enter the goal node: ")

    # Get the node details from the user.
    number_of_nodes = int(input("Enter the number of nodes: "))
    for i in range(number_of_nodes):
        node_data = input(f"Enter the data for node {i + 1}: ")
        heuristic_cost = float(input(f"Enter the heuristic cost for node {node_data}: "))
        graph.add_node(node_data, heuristic_cost)

    # Get the edge details from the user.
    number_of_edges = int(input("Enter the number of edges: "))
    for i in range(number_of_edges):
        start_node = input(f"Enter the start node for edge {i + 1}: ")
        end_node = input(f"Enter the end node for edge {i + 1}: ")
        cost = float(input(f"Enter the cost for edge {i + 1}: "))
        graph.add_edge(start_node, end_node, cost)
        graph.add_edge(end_node, start_node, cost)

    while True:
        start_node = input("Enter the start node (or 'exit' to quit): ")
        if start_node == "exit":
            break

        new_goal_node = input("Enter the goal node: ")
        if new_goal_node != goal_node:
            # The goal node has changed, so prompt the user to update
            # the heuristic cost for each node.
            for node in graph.vertices.values():
                new_heuristic_cost = float(input(f"Enter the updated heuristic cost for node {node.data}: "))
                node.heuristic = new_heuristic_cost

        cost, path = graph.astar_search(start_node, new_goal_node)
        if path is not None:
            print(f"The cost of the path is {cost}")
            print("The path of traversal is:")
            print(" -> ".join(path))
        else:
            print("No path found.")

if __name__ == "__main__":
    main()
