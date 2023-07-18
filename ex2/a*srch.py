import heapq


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}
        self.heuristics = {}

    def add_node(self, node):
        if node.strip():  # Check if node name is not empty or whitespace
            node = node.split()[0]  # Consider only the part before space if present
            if node not in self.nodes:
                self.nodes.add(node)
                return True  # Node added successfully
            else:
                print(f"Node '{node}' already exists.")
        else:
            print("Invalid node name.")

        return False  # Node addition failed

    def add_edge(self, node1, node2, cost):
        node1 = node1.split()[0]  # Consider only the part before space if present
        node2 = node2.split()[0]  # Consider only the part before space if present

        if node1 == node2:
            print("Node names in an edge cannot be the same.")
            return False

        if node1 in self.nodes and node2 in self.nodes:
            if node1 not in self.edges:
                self.edges[node1] = {}
            self.edges[node1][node2] = cost
            return True  # Edge added successfully
        else:
            print("One or both nodes do not exist.")

        return False  # Edge addition failed

    def delete_node(self, node):
        if node in self.nodes:
            self.nodes.remove(node)
            self.edges.pop(node, None)
            for edge in self.edges.values():
                edge.pop(node, None)
            return True  # Node deleted successfully
        else:
            print(f"Node '{node}' does not exist.")

        return False  # Node deletion failed

    def delete_edge(self, node1, node2):
        if node1 in self.edges and node2 in self.edges[node1]:
            del self.edges[node1][node2]
            return True  # Edge deleted successfully
        else:
            print(f"Edge ({node1} -> {node2}) does not exist.")

        return False  # Edge deletion failed

    def print_graph(self):
        for node in self.nodes:
            if node in self.edges:
                neighbors = self.edges[node].keys()
                for neighbor in neighbors:
                    cost = self.edges[node][neighbor]
                    print(f"{node} -> {neighbor} (Cost: {cost})")

    def print_adjacency_list(self):
        for node in self.nodes:
            if node in self.edges:
                neighbors = self.edges[node].keys()
                neighbor_list = ", ".join(neighbors)
                print(f"{node}: {neighbor_list}")

    def a_star_search(self, start_node, goal_node):
        if start_node not in self.nodes or goal_node not in self.nodes:
            print("One or both of the nodes do not exist.")
            return None, float('inf')

        open_set = [(0, start_node)]  # Priority queue: (f_score, node)
        closed_set = set()
        g_scores = {node: float('inf') for node in self.nodes}
        g_scores[start_node] = 0
        f_scores = {node: float('inf') for node in self.nodes}
        f_scores[start_node] = self.heuristics[start_node]

        while open_set:
            current_f, current_node = heapq.heappop(open_set)

            if current_node == goal_node:
                return self._reconstruct_path(goal_node, g_scores), g_scores[goal_node]

            closed_set.add(current_node)

            if current_node in self.edges:
                neighbors = self.edges[current_node].keys()
                for neighbor in neighbors:
                    tentative_g = g_scores[current_node] + self.edges[current_node][neighbor]
                    if tentative_g < g_scores[neighbor]:
                        g_scores[neighbor] = tentative_g
                        f_scores[neighbor] = g_scores[neighbor] + self.heuristics[neighbor]
                        if neighbor not in closed_set:
                            heapq.heappush(open_set, (f_scores[neighbor], neighbor))

        return None, float('inf')

    def _reconstruct_path(self, goal_node, g_scores):
        path = [goal_node]
        current_node = goal_node

        while current_node in self.edges:
            for neighbor, _ in self.edges[current_node].items():
                if (
                    current_node in self.edges and
                    neighbor in self.edges[current_node] and
                    g_scores[neighbor] == g_scores[current_node] - self.edges[current_node][neighbor]
                ):
                    path.append(neighbor)
                    current_node = neighbor
                    break

        path.reverse()
        return path


def build_graph():
    g = Graph()

    num_nodes = int(input("Enter the number of nodes: "))
    for i in range(num_nodes):
        node = input(f"Enter node {i + 1}: ")
        while not g.add_node(node):
            node = input("Enter a valid node name: ")

        heuristic = int(input(f"Enter heuristic cost for node {node}: "))
        g.heuristics[node] = heuristic

    num_edges = int(input("Enter the number of edges: "))
    for i in range(num_edges):
        edge = input(f"Enter edge {i + 1} (node1 node2 cost): ").split()
        node1, node2, cost = edge[0], edge[1], int(edge[2])
        while not g.add_edge(node1, node2, cost):
            edge = input("Enter a valid edge: ").split()
            node1, node2, cost = edge[0], edge[1], int(edge[2])

    return g



def switch_case(graph):
    while True:
        print("\n----- Menu -----")
        print("1. Add Node")
        print("2. Add Edge")
        print("3. Delete Node")
        print("4. Delete Edge")
        print("5. Print Graph")
        print("6. Print Adjacency List")
        print("7. A* Search")
        print("8. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            node = input("Enter the node to add: ")
            while not graph.add_node(node):
                node = input("Enter a valid node name: ")
            print(f"Node {node} added.")

        elif choice == 2:
            node1, node2, cost = input("Enter the edge (node1 node2 cost): ").split()
            while not graph.add_edge(node1, node2, int(cost)):
                print("Invalid edge.")
                node1, node2, cost = input("Enter a valid edge (node1 node2 cost): ").split()
            print(f"Edge ({node1} -> {node2}) added with cost {cost}.")

        elif choice == 3:
            node = input("Enter the node to delete: ")
            while not graph.delete_node(node):
                print(f"Node '{node}' does not exist.")
                node = input("Enter a valid node name: ")
            print(f"Node {node} deleted.")

        elif choice == 4:
            node1, node2 = input("Enter the edge to delete (node1 node2): ").split()
            while not graph.delete_edge(node1, node2):
                print(f"Edge ({node1} -> {node2}) does not exist.")
                node1, node2 = input("Enter a valid edge to delete (node1 node2): ").split()
            print(f"Edge ({node1} -> {node2}) deleted.")

        elif choice == 5:
            print("Graph:")
            graph.print_graph()

        elif choice == 6:
            print("Adjacency List:")
            graph.print_adjacency_list()

        elif choice == 7:
            start_node = input("Enter the start node: ")
            goal_node = input("Enter the goal node: ")
            path, cost = graph.a_star_search(start_node, goal_node)
            if path:
                print(f"Shortest path from {start_node} to {goal_node}: {path}")
                print(f"Cost: {cost}")
            else:
                print(f"No path found from {start_node} to {goal_node}")

        elif choice == 8:
            break

        else:
            print("Invalid choice. Please try again.")


# Example usage:
graph = build_graph()
switch_case(graph)













