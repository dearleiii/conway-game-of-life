import os
import time
import copy

from read_write import save_universe, load_universe


# Size of the grid
ROWS = 20
COLS = 40

# Time delay between generations
DELAY = 0.2

# Character representation
ALIVE = 'O'
DEAD = '.'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_grid(grid):
    clear_screen()
    for row in grid:
        print(''.join(ALIVE if cell else DEAD for cell in row))

def count_neighbors(grid, x, y):
    """
    Count and return the # of live cell neighbors 
    """
    neighbors = 0
    for i in range(-1, 2):  # [-1, 0, 1]
        for j in range(-1, 2):
            if i == 0 and j == 0:   # skip self
                continue
            nx, ny = x + i, y + j
            if 0 <= nx < ROWS and 0 <= ny < COLS:   # check within bound of grid 
                neighbors += grid[nx][ny]
    return neighbors

def next_generation(grid):
    new_grid = copy.deepcopy(grid)
    for x in range(ROWS):
        for y in range(COLS):
            neighbors = count_neighbors(grid, x, y)
            if grid[x][y] == 1:
                # Rule 1 and 3: Any live cell with two or three live neighbors survives
                # All other live cells die in the next generation
                if neighbors not in (2, 3):
                    new_grid[x][y] = 0
            else:
                # Rule 2: dead cell with exactly three live neighbors becomes a live cell;
                if neighbors == 3:
                    new_grid[x][y] = 1
    return new_grid

def initialize_grid():
    grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]

    # Add a glider pattern (top-left corner)
    glider = [
        (1, 2),
        (2, 3),
        (3, 1), (3, 2), (3, 3),
    ]

    for x, y in glider:
        grid[x][y] = 1

    return grid

def run_game():
    use_saved = input("Load universe from file? (y/n): ").lower() == 'y'
    if use_saved:
        grid = load_universe("universe.txt", ROWS, COLS)
        if grid:
            print("Universe loaded from file.")
        else:
            print(f"File not found or could not be loaded.")
            print("Starting with default glider pattern instead.")
            grid = initialize_grid()
    else:
        grid = initialize_grid()

    for i in range(10):
        time.sleep(DELAY)
    
    generations = 100
    for _ in range(generations):
        print_grid(grid)
        grid = next_generation(grid)
        time.sleep(DELAY)
    
    save_universe(grid)
    print("Universe saved to 'universe.txt'.")


if __name__ == "__main__":
    run_game()