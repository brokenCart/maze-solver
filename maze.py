import random
import time

from cell import Cell
from config import ANIMATION_SLEEP_TIME
from graphics import Window


class Maze:
    def __init__(
        self,
        x1: int,
        y1: int,
        num_cols: int,
        num_rows: int,
        cell_size_x: float,
        cell_size_y: float,
        win: Window | None = None,
        seed=None,
    ):
        self.__cells: list[list[Cell]] = []
        self.__x1 = x1
        self.__y1 = y1
        self.__num_cols = num_cols
        self.__num_rows = num_rows
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win

        if seed:
            random.seed(seed)

        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0, 0)
        self.__reset_cells_visited()

    def __create_cells(self):
        for i in range(self.__num_cols):
            self.__cells.append([])
            col = self.__cells[i]
            for j in range(self.__num_rows):
                cell = Cell(self.__win)
                col.append(cell)
                self.__draw_cell(i, j)

    def __draw_cell(self, i: int, j: int):
        self.__cells[i][j].draw(
            self.__x1 + i * self.__cell_size_x,
            self.__y1 + j * self.__cell_size_y,
            self.__x1 + (i + 1) * self.__cell_size_x,
            self.__y1 + (j + 1) * self.__cell_size_y,
        )
        self.__animate()

    def __animate(self):
        if not self.__win:
            return

        self.__win.redraw()
        time.sleep(ANIMATION_SLEEP_TIME)

    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)

        self.__cells[self.__num_cols - 1][self.__num_rows - 1].has_bottom_wall = False
        self.__draw_cell(self.__num_cols - 1, self.__num_rows - 1)

    def __break_walls_r(self, i: int, j: int):
        self.__cells[i][j].visited = True

        while True:
            possible_dir = []
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for di, dj in directions:
                next_i = i + di
                next_j = j + dj

                if not ((0 <= next_i < self.__num_cols) and (0 <= next_j < self.__num_rows)):
                    continue

                if self.__cells[next_i][next_j].visited:
                    continue

                possible_dir.append((next_i, next_j))

            if not len(possible_dir):
                self.__draw_cell(i, j)
                return

            next_i, next_j = random.choice(possible_dir)
            if next_i - i == 1:
                self.__cells[i][j].has_right_wall = False
                self.__cells[next_i][next_j].has_left_wall = False
            elif next_i - i == -1:
                self.__cells[i][j].has_left_wall = False
                self.__cells[next_i][next_j].has_right_wall = False
            elif next_j - j == 1:
                self.__cells[i][j].has_bottom_wall = False
                self.__cells[next_i][next_j].has_top_wall = False
            elif next_j - j == -1:
                self.__cells[i][j].has_top_wall = False
                self.__cells[next_i][next_j].has_bottom_wall = False

            self.__draw_cell(i, j)
            self.__draw_cell(next_i, next_j)

            self.__break_walls_r(next_i, next_j)

    def __reset_cells_visited(self):
        for col in self.__cells:
            for cell in col:
                cell.visited = False
