# 🧩 Maze Solver

A Python maze generator and solver with **real-time graphical visualization** using Tkinter. Watch as the maze is built wall-by-wall, then solved step-by-step — all animated in a live window.

- **Generation**: Recursive backtracking (randomized DFS) carves a perfect maze with a single unique solution path.
- **Solving**: Breadth-first search (BFS) finds the shortest path from entrance to exit.
- **Visualization**: Every step is animated — gray lines show BFS exploration, red lines highlight the final solution path.

## Demo

Run the program and a window will open showing:

1. The maze grid being constructed cell-by-cell
2. Walls being broken to carve passages (recursive backtracking)
3. BFS exploration radiating outward (gray lines)
4. The shortest solution path traced back from exit to entrance (red line)

## Getting Started

### Prerequisites

- **Python 3.14+**
- **Tkinter** (included with most Python installations)
- [**uv**](https://docs.astral.sh/uv/) (recommended package manager)

> [!NOTE]
> Tkinter requires a display server. On headless Linux systems, you may need to install `python3-tk` (e.g., `sudo apt install python3-tk`) and run with a display available.

### Installation

```bash
# Clone the repository
git clone https://github.com/brokenCart/maze-solver.git
cd maze-solver

# Create a virtual environment and install dependencies
uv sync
```

### Running

```bash
uv run python main.py
```

An 800×600 window will appear. Close the window when done.

## Configuration

### Maze Parameters

Maze dimensions and layout are configured directly in [`main.py`](main.py):

```python
num_rows = 12        # Number of rows in the maze
num_cols = 16        # Number of columns in the maze
margin = 50          # Pixel margin around the maze
screen_x = 800       # Window width in pixels
screen_y = 600       # Window height in pixels
```

Cell sizes are calculated automatically to fill the available space.

### Animation Speed

Adjust the animation delay in [`config.py`](config.py):

```python
ANIMATION_SLEEP_TIME = 0.02  # Seconds between animation frames
```

Lower values → faster animation. Set to `0` to skip animation delays entirely.

## How It Works

### Maze Generation — Recursive Backtracking

1. Start at cell `(0, 0)`, mark it visited
2. Randomly choose an unvisited neighbor
3. Break the wall between the current cell and the chosen neighbor
4. Recursively repeat from the new cell
5. Backtrack when no unvisited neighbors remain

This produces a **perfect maze** — every cell is reachable and there is exactly one path between any two cells.

### Maze Solving — Breadth-First Search (BFS)

1. Start BFS from the entrance cell `(0, 0)`
2. Explore all reachable neighbors level-by-level, respecting walls
3. Track each cell's predecessor to reconstruct the path
4. Once the exit cell `(num_cols-1, num_rows-1)` is reached, trace back through predecessors to draw the shortest path

**Visual cues during solving:**
- **Gray lines** — BFS exploration (cells being visited)
- **Red lines** — the final shortest solution path

## Project Structure

```
maze-solver/
├── main.py          # Entry point — configures and launches the maze
├── maze.py          # Maze class — generation (recursive backtracking) and solving (BFS)
├── cell.py          # Cell class — wall state, drawing, and move visualization
├── graphics.py      # Window, Point, and Line classes — Tkinter rendering layer
├── config.py        # Animation speed constant
├── tests.py         # Unit tests (unittest)
├── pyproject.toml   # Project metadata and dev dependencies
└── uv.lock          # Locked dependency versions
```

### Module Responsibilities

| Module | Purpose |
|---|---|
| [`main.py`](main.py) | Configures maze dimensions, creates the window, and runs the solver |
| [`maze.py`](maze.py) | Core algorithms — cell grid creation, wall-breaking generation, BFS solving |
| [`cell.py`](cell.py) | Represents a single cell with 4 walls, handles drawing walls and move lines |
| [`graphics.py`](graphics.py) | Thin Tkinter wrapper — `Window` for the canvas, `Point` and `Line` for drawing |
| [`config.py`](config.py) | Shared constants (`ANIMATION_SLEEP_TIME`) |
| [`tests.py`](tests.py) | Unit tests for grid creation, entrance/exit walls, visited reset, wall-breaking, and solving |

## Testing

Run the test suite (no GUI window needed — tests run headless):

```bash
uv run python -m unittest tests.py -v
```

The tests verify:
- Correct grid dimensions are created
- Entrance and exit walls are properly removed
- Cell `visited` flags reset correctly after generation
- Wall-breaking connects adjacent cells as expected
- The solver successfully finds a path

## Tech Stack

- **Python 3.14** — core language
- **Tkinter** — GUI rendering (stdlib, no external deps)
- **uv** — package and environment management
- **ruff** — linting and formatting
- **isort** — import sorting
