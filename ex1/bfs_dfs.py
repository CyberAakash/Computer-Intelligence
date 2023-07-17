from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, data):
        if data not in self.vertices:
            self.vertices[data] = None

    def add_edge(self, src, dest):
        if src not in self.vertices:
            self.add_vertex(src)

        if dest not in self.vertices:
            self.add_vertex(dest)

        new_node = Node(dest)
        new_node.next = self.vertices[src]
        self.vertices[src] = new_node

    def display_graph(self):
        for vertex in self.vertices:
            print(f"Vertex {vertex}: ", end="")
            current_node = self.vertices[vertex]
            while current_node:
                print(f"{current_node.data} -> ", end="")
                current_node = current_node.next
            print("None")

    def dfs(self, start, destination):
        visited = set()
        stack = [start]

        while stack:
            current_vertex = stack.pop()
            print(current_vertex, end=" ")

            if current_vertex == destination:
                print("\nReached destination!")
                return

            visited.add(current_vertex)
            current_node = self.vertices[current_vertex]

            while current_node:
                if current_node.data not in visited:
                    stack.append(current_node.data)
                current_node = current_node.next

        print("\nDestination not found!")
    def bfs(self, start, destination):
        visited = set()
        queue = deque([start])

        while queue:
            current_vertex = queue.popleft()
            print(current_vertex, end=" ")

            if current_vertex == destination:
                print("\nReached destination!")
                return

            visited.add(current_vertex)
            current_node = self.vertices[current_vertex]

            while current_node:
                if current_node.data not in visited:
                    queue.append(current_node.data)
                    visited.add(current_node.data)
                current_node = current_node.next

        print("\nDestination not found!")

# Example usage
def main():
    graph = Graph()
    while(1):
        print("1.Add new Vertices")
        print("2.Add new Edge")
        print("3.Display Graph")
        print("4.Traverse the Graph using DFS")
        print("5.Traverse the Graph using BFS")
        print("6.Exit")
        print("Enter your choice:")
        ch = eval(input())
        if(ch == 1):
            print("Enter the data for node:")
            data = input()
            graph.add_vertex(data)
        elif(ch == 2):
            print("Enter the source vertex")
            src = input()
            print("Enter the destination vertex")
            dest = input()
            graph.add_edge(src, dest)
        elif(ch == 3):
            print("The Graph is")
            graph.display_graph()
        elif(ch == 4):
            print("Enter the source vertex")
            src = input()
            print("Enter the destination vertex")
            dest = input()
            print("DFS Traversal:")
            graph.dfs(src, dest)
        elif(ch == 5):
            print("Enter the source vertex")
            src = input()
            print("Enter the destination vertex")
            dest = input()
            print("BFS Traversal:")
            graph.bfs(src, dest)
        elif(ch == 6):
            break
        else:
            print("Wrong input!!!")

if __name__ == "__main__":
    main()