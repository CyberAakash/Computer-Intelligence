import random
from collections import deque

class WumpusWorld:
    def __init__(self, size):
        self.size = size
        self.grid = [[Cell() for _ in range(size)] for _ in range(size)]
        self.agent_pos = (size - 1, 0)  # Starting from bottom left
        self.agent_direction = "right"  # Starting direction
        self.generate_world()
 
    def generate_world(self):
        wumpus_x, wumpus_y = self.random_position()
        self.grid[wumpus_x][wumpus_y].has_wumpus = True
        num_pits = min(3, self.size * self.size - 1)  # Limiting the number of pits to 3
        for _ in range(num_pits):
            pit_x, pit_y = self.random_position()
            self.grid[pit_x][pit_y].has_pit = True
            # Mark adjacent cells as having breeze
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_x, new_y = pit_x + dx, pit_y + dy
                if (new_x, new_y) == self.agent_pos:
                    continue  # Skip marking the starting cell
                if 0 <= new_x < self.size and 0 <= new_y < self.size:
                    self.grid[new_x][new_y].has_breeze = True
        gold_x, gold_y = self.random_position()
        self.grid[gold_x][gold_y].has_gold = True
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j].has_wumpus:
                    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        if 0 <= i + dx < self.size and 0 <= j + dy < self.size:
                            self.grid[i + dx][j + dy].has_stench = True
                if self.grid[i][j].has_gold:
                    self.grid[i][j].has_glitter = True  
    def random_position(self):
        x = random.randint(0, self.size - 1)
        y = random.randint(0, self.size - 1)
        return x, y
    def print_world(self):
        for i in range(self.size):
            for j in range(self.size):
                cell = self.grid[i][j]
                if (i, j) == self.agent_pos:
                    if self.agent_direction == "up":
                        print("^", end="\t")
                    elif self.agent_direction == "down":
                        print("v", end="\t")
                    elif self.agent_direction == "left":
                        print("<", end="\t")
                    else:
                        print(">", end="\t")
                else:
                    symbols = ""
                    if cell.has_wumpus:
                        symbols += "w"
                    if cell.has_pit:
                        symbols += "P"
                    if cell.has_gold:
                        symbols += "G"
                    if cell.has_stench:
                        symbols += "S"
                    if cell.has_breeze:
                        symbols += "B"
                    if cell.has_glitter:
                        symbols += "gl"
                    if symbols:
                        print(symbols, end="\t")
                    else:
                        print("-", end="\t")
            print("\n")
    def bfs(self, start, goal):
        queue = deque([(start, [])])
        visited = set()

        while queue:
            current, path = queue.popleft()
            if current == goal:
                return path
            if current in visited:
                continue
            visited.add(current)

            x, y = current
            neighbors = self.get_valid_neighbors(x, y)
            for neighbor in neighbors:
                n_x, n_y = neighbor
                if self.grid[n_x][n_y].has_pit:
                    continue  # Skip paths leading to pits
                queue.append((neighbor, path + [neighbor]))

        return None

    def get_valid_neighbors(self, x, y):
        neighbors = []
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < self.size and 0 <= new_y < self.size:
                neighbors.append((new_x, new_y))
        return neighbors

    def find_gold(self):
        start = (self.agent_pos[0], self.agent_pos[1])
        gold_pos = self.get_gold_position()

        if not gold_pos:
            return []

        path = self.bfs(start, gold_pos)
        return path

    def get_gold_position(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j].has_gold:
                    return i, j
        return None

    def play(self):
        optimal_path = self.find_gold()

        if not optimal_path:
            print("No path to the gold.")
            return

        print("Optimal path to the gold:", optimal_path)
        self.print_world()
        for step, (x, y) in enumerate(optimal_path):
            self.agent_pos = (x, y)
            # print(f"Step {step + 1}: Agent at position ({(x+1)%5}, {(y+1)%5})")
            print("Next Step.")
            self.print_world()
            
            if self.grid[x][y].has_gold:
                print("Congratulations! You found the gold and won!")
                break

class Cell:
    def __init__(self):
        self.visited = False
        self.has_wumpus = False
        self.has_pit = False
        self.has_gold = False
        self.has_stench = False
        self.has_breeze = False
        self.has_glitter = False

def main():
    size = 4  # You can change the size of the grid
    game = WumpusWorld(size)
    game.play()

if __name__ == "__main__":
    main()
