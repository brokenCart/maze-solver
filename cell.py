from graphics import Line, Point, Window


class Cell:
    def __init__(self, window: Window | None = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1.0
        self.__y1 = -1.0
        self.__x2 = -1.0
        self.__y2 = -1.0
        self.__win = window

    def draw(self, x1, y1, x2, y2):
        if not self.__win:
            return

        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

        line = Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2))
        self.__win.draw_line(line, "black" if self.has_left_wall else "white")

        line = Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2))
        self.__win.draw_line(line, "black" if self.has_right_wall else "white")

        line = Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
        self.__win.draw_line(line, "black" if self.has_top_wall else "white")

        line = Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2))
        self.__win.draw_line(line, "black" if self.has_bottom_wall else "white")

    def draw_move(self, to_cell: "Cell", undo: bool = False):
        if not self.__win:
            return

        fill_color = "gray" if undo else "red"
        self_center = Point((self.__x1 + self.__x2) / 2, (self.__y1 + self.__y2) / 2)
        to_cell_center = Point(
            (to_cell.__x1 + to_cell.__x2) / 2, (to_cell.__y1 + to_cell.__y2) / 2
        )
        line = Line(self_center, to_cell_center)
        self.__win.draw_line(line, fill_color)
