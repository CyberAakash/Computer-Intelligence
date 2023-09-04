from collections import deque

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_node(self, node):
        if node not in self.adj_list:
            self.adj_list[node] = []

    def add_edge(self, node1, node2):
        if node1 in self.adj_list and node2 in self.adj_list:
            self.adj_list[node1].append(node2)
            self.adj_list[node2].append(node1)

    def delete_node(self, node):
        if node in self.adj_list:
            del self.adj_list[node]
            for adj_nodes in self.adj_list.values():
                if node in adj_nodes:
                    adj_nodes.remove(node)

    def delete_edge(self, node1, node2):
        if node1 in self.adj_list and node2 in self.adj_list:
            if node2 in self.adj_list[node1]:
                self.adj_list[node1].remove(node2)
            if node1 in self.adj_list[node2]:
                self.adj_list[node2].remove(node1)

    def print_adjacency_list(self):
        for node, adj_nodes in self.adj_list.items():
            print(f"{node}: {', '.join(adj_nodes)}")

    def print_graph(self):
        print("Graph:")
        for node, adj_nodes in self.adj_list.items():
            if adj_nodes:
                print(f"{node} -> {', '.join(adj_nodes)}")
            else:
                print(node)

    def bfs(self, start_node, goal_node):
        visited = set()
        queue = deque([(start_node, [start_node])])
        visited.add(start_node)

        print("BFS Traversal:")
        while queue:
            current_node, path = queue.popleft()
            print(current_node, end=" ")

            if current_node == goal_node:
                print("\nGoal node reached.")
                print("Path:", "->".join(path))
                return

            for neighbor in self.adj_list[current_node]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
                    visited.add(neighbor)

    def build_graph(self):
        num_nodes = int(input("Enter the number of nodes: "))
        num_edges = int(input("Enter the number of edges: "))

        for i in range(num_nodes):
            node = input(f"Enter node {i + 1}: ")
            self.add_node(node)

        print("Enter the edges:")
        for i in range(num_edges):
            node1 = input(f"Enter the first node of edge {i + 1}: ")
            node2 = input(f"Enter the second node of edge {i + 1}: ")
            self.add_edge(node1, node2)

# Example usage
graph = Graph()

while True:
    print("\nOperations:")
    print("1. Build Graph")
    print("2. Add Node")
    print("3. Add Edge")
    print("4. Delete Node")
    print("5. Delete Edge")
    print("6. Print Adjacency List")
    print("7. Print Graph")
    print("8. BFS Traversal")
    print("9. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        graph.build_graph()
    elif choice == 2:
        node = input("Enter node: ")
        graph.add_node(node)
    elif choice == 3:
        node1 = input("Enter first node: ")
        node2 = input("Enter second node: ")
        graph.add_edge(node1, node2)
    elif choice == 4:
        node = input("Enter node to delete: ")
        graph.delete_node(node)
    elif choice == 5:
        node1 = input("Enter first node: ")
        node2 = input("Enter second node: ")
        graph.delete_edge(node1, node2)
    elif choice == 6:
        graph.print_adjacency_list()
    elif choice == 7:
        graph.print_graph()
    elif choice == 8:
        start_node = input("Enter the starting node for BFS: ")
        goal_node = input("Enter the goal node for BFS: ")
        graph.bfs(start_node, goal_node)
    elif choice == 9:
        break
    else:
        print("Invalid choice. Please try again.")
