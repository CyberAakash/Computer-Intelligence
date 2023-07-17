from collections import deque

def bfs(graph, start):
    visited = set()  # Set to keep track of visited nodes
    queue = deque([start])  # Initialize the queue with the starting node

    while queue:
        vertex = queue.popleft()  # Get the next node from the queue
        print(vertex)  # Process the node (print or do something else)

        # Add the current node to the visited set
        visited.add(vertex)

        # Visit all neighboring nodes of the current node
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)  # Add neighboring node to the queue

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

bfs(graph, 'A')
