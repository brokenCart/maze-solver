# Maze Solver

Maze Solver is an interactive Python application that generates and solves mazes with real-time graphical visualization using Tkinter.

## Description

This project generates mazes using a randomized depth-first search algorithm (recursive backtracking) and solves them using Breadth-First Search (BFS). As the maze is built and solved, the process is animated step-by-step on a Tkinter canvas. Gray lines illustrate the path discovery phase during search, while red lines highlight the final shortest solution path from entrance to exit.

## Key Features

- Real-Time Graphical Animation: Live visualization of cell creation, wall carving, and pathfinding exploration.
- Recursive Backtracking Generation: Carves out a perfect maze with a single unique solution path between entrance and exit.
- Breadth-First Search (BFS) Solver: Explores valid paths systematically to guarantee finding the shortest solution path.
- Configurable Dimensions and Animation: Easily adjust grid rows, columns, canvas size, margins, and animation delays.
- Lightweight with Minimal Dependencies: Built using Python standard library features and Tkinter for rendering.
- Automated Test Suite: Includes unit tests covering maze initialization, wall breaking, state resets, and solver validation.

## Installation

### Prerequisites

- Python 3.14 or higher
- Tkinter (included with standard Python installations)
- uv package manager (recommended)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/brokenCart/maze-solver.git
   cd maze-solver
   ```

2. Synchronize environment and dependencies:
   ```bash
   uv sync
   ```

## Usage

Run the main application:

```bash
uv run python main.py
```

### Running Tests

Execute the unit test suite:

```bash
uv run python -m unittest tests.py -v
```

## Project Structure

- `main.py`: Entry point for configuring maze parameters and starting the application.
- `maze.py`: Core algorithm logic for maze generation and BFS solving.
- `cell.py`: Represents individual maze cells and manages wall drawing and movement paths.
- `graphics.py`: Tkinter graphics wrapper providing canvas, window, point, and line drawing utilities.
- `config.py`: Application configurations such as animation sleep duration.
- `tests.py`: Headless unit tests for verifying core maze functionalities.
