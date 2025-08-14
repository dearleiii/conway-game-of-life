import time

from game_of_life_sparse import print_sparse_auto_pan, next_generation_sparse
from read_write import save_universe_sparse, load_universe_sparse

# Set max view and padding, to track the view of gliders
MAX_VIEW = 40
PADDING = 5


def initialize_gosper_glider_gun(offset_x=0, offset_y=0):
    """
    Default: places the gun around (0, 0)
    """
    pattern = [
        (5, 1), (5, 2), (6, 1), (6, 2),
        (5, 11), (6, 11), (7, 11), (4, 12), (8, 12), (3, 13), (9, 13),
        (3, 14), (9, 14), (6, 15), (4, 16), (8, 16), (5, 17), (6, 17), (7, 17),
        (6, 18),
        (3, 21), (4, 21), (5, 21), (3, 22), (4, 22), (5, 22),
        (2, 23), (6, 23),
        (1, 25), (2, 25), (6, 25), (7, 25),
        (3, 35), (4, 35), (3, 36), (4, 36),
    ]
    return {(x + offset_x, y + offset_y) for x, y in pattern}


# Can offset to a large coordinates
live_cells = initialize_gosper_glider_gun(offset_x=0, offset_y=0)


def run_sparse_game_auto_pan():
    live_cells = initialize_gosper_glider_gun(offset_x=0, offset_y=0)
    generations = 200

    for _ in range(generations):
        print_sparse_auto_pan(live_cells, padding=PADDING, max_view=MAX_VIEW)
        live_cells = next_generation_sparse(live_cells)
        time.sleep(0.1)


if __name__ == "__main__":
    run_sparse_game_auto_pan()