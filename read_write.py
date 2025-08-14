# Size of the grid
ROWS = 20
COLS = 40

# Time delay between generations
DELAY = 0.2

# Character representation
ALIVE = 'O'
DEAD = '.'


def save_universe(grid, filename="universe.txt"):
    with open(filename, "w") as f:
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    f.write(f"{x} {y}\n")


def save_universe_sparse(live_cells, filename="universe.txt"):
    with open(filename, "w") as f:
        for x, y in sorted(live_cells):
            f.write(f"{x} {y}\n")


def load_universe(filename="universe.txt", rows=ROWS, cols=COLS):
    grid = [[0 for _ in range(cols)] for _ in range(rows)]
    try:
        with open(filename, "r") as f:
            for line in f:
                if line.strip() and not line.startswith("#"):
                    x, y = map(int, line.strip().split())
                    if 0 <= x < rows and 0 <= y < cols:
                        grid[x][y] = 1
        return grid
    except FileNotFoundError:
        print(f"File '{filename}' not found. Starting with empty universe.")
        return False
    

def load_universe_sparse(filename="universe.txt"):
    try:
        live_cells = set()
        with open(filename, "r") as f:
            for line in f:
                if line.strip() and not line.startswith("#"):
                    x, y = map(int, line.strip().split())
                    live_cells.add((x, y))
        return live_cells
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return False