"""
Implement the “very large” (2^32 by 2^32) universe by using sparse representation.
- We store only the coordinates of live cells in a set
- doesn't explicitly set a grid size like 2^32 × 2^32, it supports a huge or even infinite universe by avoiding a fixed grid entirely
- Implement visualization that automatically pans the view to show the alive pattern(s).
"""

import os
import time
import copy
from collections import defaultdict

from read_write import save_universe_sparse, load_universe_sparse

        
# Time delay between generations
DELAY = 0.2

# Character representation
ALIVE = 'O'
DEAD = '.'

# Auto-Panning the view to show the alive pattern(s)
AUTO_PAN = True

# Sparse representation: only live cells
LiveCells = set()

# Neighbor offsets
NEIGHBOR_OFFSETS = [ 
    (dx, dy) for dx in (-1, 0, 1)
    for dy in (-1, 0, 1)
    if not (dx == 0 and dy == 0)
]


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Sparse Update Logic
def next_generation_sparse(live_cells):
    """
    live_cells: a set of (x, y) tuples, each representing the coordinates of a currently live cell.
        This sparse representation avoids storing a huge 2D grid, making it scalable to very large universes.
    """

    # dictionary stores the number of live neighbors each cell has
    # Keys = cell coordinates (x, y)
    # Values = count of how many live cells surround that cell
    neighbor_counts = defaultdict(int)

    # Iterate through each cell 8 neighbors, count neighbors of all live cells
    for x, y in live_cells:
        for dx, dy in NEIGHBOR_OFFSETS:
            neighbor = (x + dx, y + dy)
            neighbor_counts[neighbor] += 1

    new_live_cells = set()

    for cell, count in neighbor_counts.items():
        if cell in live_cells:
            if count in (2, 3):
                new_live_cells.add(cell)  # survives
        else:
            # Rule 2: all dead cells surrounding live cells get counted
            if count == 3:
                new_live_cells.add(cell)  # birth

    return new_live_cells

# Sparse Visualization (Limited Viewport)
def print_sparse(live_cells, center=(0,0), size=20):
    clear_screen()
    cx, cy = center
    for x in range(cx, cx + size):
        row = ''
        for y in range(cy, cy + size):
            row += 'O' if (x, y) in live_cells else '.'
        print(row)


def print_sparse_auto_pan(live_cells, padding=2, max_view=20):
    """
    This function calculates the bounding box of live cells and centers the display around them.
    """
    clear_screen()

    if not live_cells:
        print("All cells are dead.")
        return

    # Get bounds of the live cell area
    xs = [x for x, _ in live_cells]
    ys = [y for _, y in live_cells]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)

    # Add some padding for visibility
    min_x -= padding
    max_x += padding
    min_y -= padding
    max_y += padding

    # Clamp to max view size to keep terminal display manageable
    height = min(max_x - min_x + 1, max_view)
    width = min(max_y - min_y + 1, max_view)

    # Print the universe within bounds
    for x in range(min_x, min_x + height):
        row = ''
        for y in range(min_y, min_y + width):
            row += 'O' if (x, y) in live_cells else '.'
        print(row)


# Initialize Sparse Glider
def initialize_sparse_glider(x=0, y=0):
    return {
        (x + 1, y + 2),
        (x + 2, y + 3),
        (x + 3, y + 1), (x + 3, y + 2), (x + 3, y + 3),
    }


def run_sparse_game():
    use_saved = input("Load universe from file? (y/n): ").lower() == 'y'
    live_cells = initialize_sparse_glider()
    center = (0, 0)

    generations = 100
    for _ in range(generations):
        if AUTO_PAN: 
            print_sparse_auto_pan(live_cells)
        else: 
            print_sparse(live_cells, center=center, size=20)
        live_cells = next_generation_sparse(live_cells)
        time.sleep(DELAY)


if __name__ == "__main__":
    run_sparse_game()