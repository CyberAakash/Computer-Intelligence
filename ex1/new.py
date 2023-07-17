import collections

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = collections.defaultdict(list)

    def add_node(self, node):
        self.nodes.add(node)

    def add_edge(self, node1, node2, cost=0):
        self.edges[node1].append((node2, cost))
        self.edges[node2].append((node1, cost))

    def bfs(self, start_node):
        visited = set()
        queue = collections.deque([start_node])

        while queue:
            node = queue.popleft()
            if node in visited:
                continue

            visited.add(node)
            print(node)

            for neighbor, cost in self.edges[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

    def dfs(self, start_node):
        visited = set()
        stack = [start_node]

        while stack:
            node = stack.pop()
            if node in visited:
                continue

            visited.add(node)
            print(node)

            for neighbor, cost in self.edges[node]:
                if neighbor not in visited:
                    stack.append(neighbor)

    def uniform_cost_search(self, start_node, goal_node):
        visited = set()
        queue = collections.deque([(start_node, 0)])

        while queue:
            node, cost = queue.popleft()
            if node in visited:
                continue

            visited.add(node)
            if node == goal_node:
                return cost

            for neighbor, cost_to_neighbor in self.edges[node]:
                if neighbor not in visited:
                    queue.append((neighbor, cost + cost_to_neighbor))

    def delete_node(self, node):
        if node in self.nodes:
            self.nodes.remove(node)
            self.edges.pop(node, None)  # Remove all edges connected to the node

            for neighbor, edges in self.edges.items():
                self.edges[neighbor] = [(n, c) for n, c in edges if n != node]

    def delete_edge(self, node1, node2):
        if node1 in self.nodes and node2 in self.nodes:
            self.edges[node1] = [(n, c) for n, c in self.edges[node1] if n != node2]
            self.edges[node2] = [(n, c) for n, c in self.edges[node2] if n != node1]

    def display_graph(self):
        print("Nodes:")
        for node in self.nodes:
            print(node)
        print("Edges:")
        for node, neighbors in self.edges.items():
            for neighbor, cost in neighbors:
                print(f"{node} --({cost})--> {neighbor}")
    def get_input(self):
        nodes = []
        while True:
            node = input("Enter a node: ")
            if node == "":
                break
            nodes.append(node)

        edges = []
        while True:
            edge = input("Enter an edge (node1, node2, cost): ")
            if edge == "":
                break
            edge_data = edge.split(",")
            if len(edge_data) != 3:
                print("Invalid edge format")
                continue
            node1, node2, cost = edge_data
            edges.append((node1, node2, int(cost)))

        for node in nodes:
            self.add_node(node)
        for edge in edges:
            self.add_edge(*edge)

    def menu(self):
        print("1. Get Input")
        print("2. Add a node")
        print("3. Add an edge")
        print("4. Delete a node")
        print("5. Delete an edge")
        print("6. BFS")
        print("7. DFS")
        print("8. Uniform Cost Search")
        print("9. Display Graph")
        print("10. exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            self.get_input()

        elif choice == 2:
            node = input("Enter a node name: ")
            self.add_node(node)

        elif choice == 3:
            node1, node2, cost = input("Enter the first node name: "), input(
                "Enter the second node name: "), int(input("Enter the cost: "))
            self.add_edge(node1, node2, cost)

        elif choice == 4:
            node = input("Enter the node name: ")
            self.delete_node(node)
        elif choice == 5:
            node1 = input("Enter the node name 1:")
            node2 = input("Enter the node name 2:")
            self.delete_edge(node1,node2)
        elif choice == 6:
            print("The BFS traversal is: ")
            self.bfs(input("Enter the start node: "))
        elif choice == 7:
            print("The DFS traversal is: ")
            self.dfs(input("Enter the start node: "))
        elif choice == 8:
            print("The cost of the shortest path from {} to {} is {}".format(
                input("Enter the start node: "), input("Enter the goal node: "),
                self.uniform_cost_search(input("Enter the start node: "),
                                         input("Enter the goal node: "))))
        elif choice == 9:
            self.display_graph()
        elif choice == 10:
            exit()
        else:
            print("Invalid choice")

if __name__ == "__main__":
    graph = Graph()

    while True:
        graph.menu()