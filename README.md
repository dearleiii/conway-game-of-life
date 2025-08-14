# 🧬 Conway's Game of Life (With Sparse Implementation)

This project is a terminal-based simulation of **Conway's Game of Life**, implemented using both a basic matrix version and a **sparse data structure** to support a theoretically infinite universe.

---

## 🌌 Features

- ✅ Infinite grid using sparse set representation
- ✅ Dynamically auto-panning viewport
- ✅ Terminal animation with glider pattern
- ✅ Load/Save universe from/to file
- ✅ Memory-efficient: stores only live cells
- ✅ Easily handles very large coordinate spaces (e.g., `2^32 × 2^32`)

---

## 🔧 How It Works

### 🔲 Sparse Universe

Instead of using a large 2D array, we represent the grid with a Python `set` containing only the coordinates of **live cells**:

```
python
live_cells = {(x1, y1), (x2, y2), ...}
```

###  Start the Simulation

For basic matrix version:
```
python game_of_life.py 
```
For **sparse data structure** to support a theoretically infinite universe:
```
python game_of_life_sparse.py
```

It will automatically:

- Load the universe from a file (universe.txt) if available

- Fall back to a default glider pattern if the file is missing

- Save the final universe state after the simulation ends


###  Paramters

```
- Store / read path: currently hard-coded "universe.txt", can be modified

- AUTO_PAN: whether to automatically pans the view to show the live patterns 

- MAX_VIEW, PADDING: params to adjust the visualization size in terminal 
```