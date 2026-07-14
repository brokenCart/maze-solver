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
        num_rows: int,
        num_cols: int,
        cell_size_x: float,
        cell_size_y: float,
        win: Window | None = None,
        seed = None,
    ):
        self.__cells: list[list[Cell]] = []
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
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
        for i in range(self.__num_rows):
            self.__cells.append([])
            row = self.__cells[i]
            for j in range(self.__num_cols):
                cell = Cell(self.__win)
                row.append(cell)
                self.__draw_cell(i, j)

    def __draw_cell(self, row: int, col: int):
        self.__cells[row][col].draw(
            self.__x1 + col * self.__cell_size_x,
            self.__y1 + row * self.__cell_size_y,
            self.__x1 + (col + 1) * self.__cell_size_x,
            self.__y1 + (row + 1) * self.__cell_size_y,
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

        self.__cells[self.__num_rows - 1][self.__num_cols - 1].has_bottom_wall = False
        self.__draw_cell(self.__num_rows - 1, self.__num_cols - 1)
    
    def __break_walls_r(self, i: int, j: int):
        self.__cells[i][j].visited = True

        while True:
            possible_dir = []
            dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for n in range(4):
                y = i + dir[n][1]
                x = j + dir[n][0]

                if not ((0 <= x < self.__num_cols) and (0 <= y < self.__num_rows)):
                    continue

                if self.__cells[y][x].visited:
                    continue

                possible_dir.append((y, x))
            
            if not len(possible_dir):
                self.__draw_cell(i, j)
                return
            
            y, x = random.choice(possible_dir)
            if x - j == 1 and y - i == 0:
                self.__cells[i][j].has_right_wall = False
                self.__cells[y][x].has_left_wall = False
            elif x - j == -1 and y - i == 0:
                self.__cells[i][j].has_left_wall = False
                self.__cells[y][x].has_right_wall = False
            # 1 means down and -1 means up
            elif x - j == 0 and y - i == 1:
                self.__cells[i][j].has_bottom_wall = False
                self.__cells[y][x].has_top_wall = False
            elif x - j == 0 and y - i == -1:
                self.__cells[i][j].has_top_wall = False
                self.__cells[y][x].has_bottom_wall = False
            
            self.__draw_cell(i, j)
            self.__draw_cell(y, x)

            self.__break_walls_r(y, x)
    
    def __reset_cells_visited(self):
        for row in self.__cells:
            for cell in row:
                cell.visited = False
