import heapq


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}
        self.heuristics = {}

    def add_node(self, node):
        self.nodes.add(node)

    def add_edge(self, node1, node2, cost):
        if node1 not in self.edges:
            self.edges[node1] = {}
        self.edges[node1][node2] = cost

    def delete_node(self, node):
        self.nodes.remove(node)
        self.edges.pop(node, None)
        for edge in self.edges.values():
            edge.pop(node, None)

    def delete_edge(self, node1, node2):
        if node1 in self.edges and node2 in self.edges[node1]:
            del self.edges[node1][node2]

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
        open_set = [(0, start_node)]  # Priority queue: (f_score, node)
        closed_set = set()
        g_scores = {node: float('inf') for node in self.nodes}
        g_scores[start_node] = 0
        f_scores = {node: float('inf') for node in self.nodes}
        f_scores[start_node] = self.heuristics[start_node]

        while open_set:
            current_f, current_node = heapq.heappop(open_set)

            if current_node == goal_node:
                return self._reconstruct_path(goal_node, g_scores)

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

        return None

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
        g.add_node(node)

    num_edges = int(input("Enter the number of edges: "))
    for i in range(num_edges):
        edge = input(f"Enter edge {i + 1} (node1 node2 cost): ").split()
        node1, node2, cost = edge[0], edge[1], int(edge[2])
        g.add_edge(node1, node2, cost)

    return g


# Example usage:
graph = build_graph()

print("Graph:")
graph.print_graph()

start_node = input("Enter the start node: ")
goal_node = input("Enter the goal node: ")

path = graph.a_star_search(start_node, goal_node)
if path:
    print(f"Shortest path from {start_node} to {goal_node}: {path}")
else:
    print(f"No path found from {start_node} to {goal_node}")
