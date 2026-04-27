import time
import os
import random

def create_grid(rows, cols):
    return [[random.choice([0, 1]) for _ in range(cols)] for _ in range(rows)]

def print_grid(grid):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in grid:
        print("".join(["#" if cell else " " for cell in row]))

def get_neighbors(grid, r, c):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            nr, nc = r + i, c + j
            if 0 <= nr < 30 and 0 <= nc < 30:
                count += grid[nr][nc]
    return count

def update(grid):
    new_grid = [[0 for _ in range(30)] for _ in range(30)]
    for r in range(30):
        for c in range(30):
            neighbors = get_neighbors(grid, r, c)
            if grid[r][c] == 1:
                if neighbors in [2, 3]:
                    new_grid[r][c] = 1
            else:
                if neighbors == 3:
                    new_grid[r][c] = 1
    return new_grid

def main():
    grid = create_grid(30, 30)
    try:
        while True:
            print_grid(grid)
            grid = update(grid)
            time.sleep(0.1)
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
