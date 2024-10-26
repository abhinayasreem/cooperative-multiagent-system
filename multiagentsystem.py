import random

class Grid:
    def __init__(self, size, num_items):
        self.size = size
        self.grid = [[' ' for _ in range(size)] for _ in range(size)]
        self.items = []
        self.populate_items(num_items)

    def populate_items(self, num_items):
        while len(self.items) < num_items:
            x, y = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
            if (x, y) not in self.items:
                self.items.append((x, y))
                self.grid[x][y] = 'I'  # 'I' represents an item

    def display(self):
        for row in self.grid:
            print(' '.join(row))
        print()

class Agent:
    def __init__(self, name, grid):
        self.name = name
        self.grid = grid
        self.position = (random.randint(0, grid.size - 1), random.randint(0, grid.size - 1))
        self.collected_items = 0

    def move(self):
        x, y = self.position
        direction = random.choice([(0, 1), (1, 0), (0, -1), (-1, 0)])  # right, down, left, up
        new_x, new_y = x + direction[0], y + direction[1]
        
        if 0 <= new_x < self.grid.size and 0 <= new_y < self.grid.size:
            self.position = (new_x, new_y)

    def collect_item(self):
        if self.position in self.grid.items:
            self.grid.items.remove(self.position)
            self.grid.grid[self.position[0]][self.position[1]] = ' '  # Remove item from grid
            self.collected_items += 1
            print(f"{self.name} collected an item at {self.position}.")

    def act(self):
        self.move()
        self.collect_item()

def main():
    grid_size = 5
    num_items = 5
    num_agents = 2

    grid = Grid(grid_size, num_items)
    agents = [Agent(f"Agent {i+1}", grid) for i in range(num_agents)]

    print("Initial Grid:")
    grid.display()

    for _ in range(10):  # Simulate 10 time steps
        for agent in agents:
            agent.act()
        grid.display()

    total_collected = sum(agent.collected_items for agent in agents)
    print(f"Total items collected: {total_collected}")

if __name__ == "__main__":
    main()