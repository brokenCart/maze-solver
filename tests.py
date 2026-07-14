import unittest

from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_cols, num_rows, 10, 10)
        self.assertEqual(
            len(getattr(m1, "_Maze__cells")),
            num_cols,
        )
        self.assertEqual(
            len(getattr(m1, "_Maze__cells")[0]),
            num_rows,
        )

    def test_maze_create_cells_large(self):
        num_cols = 16
        num_rows = 12
        m1 = Maze(0, 0, num_cols, num_rows, 10, 10)
        self.assertEqual(
            len(getattr(m1, "_Maze__cells")),
            num_cols,
        )
        self.assertEqual(
            len(getattr(m1, "_Maze__cells")[0]),
            num_rows,
        )

    def test_maze_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_cols, num_rows, 10, 10)
        self.assertEqual(
            getattr(m1, "_Maze__cells")[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            getattr(m1, "_Maze__cells")[num_cols - 1][num_rows - 1].has_bottom_wall,
            False,
        )

    def test_maze_reset_cells_visited(self):
        num_cols = 10
        num_rows = 10
        m1 = Maze(0, 0, num_cols, num_rows, 10, 10)
        cells = getattr(m1, "_Maze__cells")
        for i in range(num_cols):
            for j in range(num_rows):
                self.assertFalse(
                    cells[i][j].visited, f"Cell at ({i}, {j}) was not reset"
                )

        # Manually set some cells to visited = True
        cells[0][0].visited = True
        cells[5][5].visited = True
        cells[num_cols - 1][num_rows - 1].visited = True

        # Call reset cells visited method
        getattr(m1, "_Maze__reset_cells_visited")()

        # Check they are reset to False
        for i in range(num_cols):
            for j in range(num_rows):
                self.assertFalse(
                    cells[i][j].visited,
                    f"Cell at ({i}, {j}) was not reset after manual trigger",
                )

    def test_maze_vertical_wall_breaking(self):
        num_cols = 1
        num_rows = 2
        m1 = Maze(0, 0, num_cols, num_rows, 10, 10, seed=42)
        cells = getattr(m1, "_Maze__cells")
        # (0, 0) is connected to (0, 1)
        # Therefore, (0, 0) should have has_bottom_wall = False, and (0, 1) has_top_wall = False
        self.assertFalse(
            cells[0][0].has_bottom_wall, "Cell (0, 0) bottom wall should be broken"
        )
        self.assertFalse(
            cells[0][1].has_top_wall, "Cell (0, 1) top wall should be broken"
        )


if __name__ == "__main__":
    unittest.main()
