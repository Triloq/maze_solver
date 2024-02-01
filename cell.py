from graphics import Line, Point

class Cell():
    def __init__(self, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = window

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self._win:
            if self.has_left_wall:
                line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
                self._win.draw_line(line, 'black')
            if self.has_top_wall:
                line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
                self._win.draw_line(line, 'black')
            if self.has_right_wall:
                line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
                self._win.draw_line(line, 'black')
            if self.has_bottom_wall:
                line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
                self._win.draw_line(line, 'black')
    
    def draw_move(self, to_cell, undo=False):
        x_s = (self._x2 + self._x1)//2
        y_s = (self._y2 + self._y1)//2
        x_t = (to_cell._x2 + to_cell._x1)//2
        y_t = (to_cell._y2 + to_cell._y1)//2
        fill = 'gray'

        if undo == False:
            fill = 'red'

        # cardinal line movement only
        # left
        if self._x1 > to_cell._x1:
            line1 = Line(Point(x_s, y_s), Point(self._x1, y_s))
            line2 = Line(Point(x_t, y_t), Point(to_cell._x2, y_t))
            self._win.draw_line(line1, fill)
            self._win.draw_line(line2, fill)

        # right
        elif self._x1 < to_cell._x1:
            line1 = Line(Point(x_s, y_s), Point(self._x2, y_s))
            line2 = Line(Point(x_t, y_t), Point(to_cell._x1, y_t))
            self._win.draw_line(line1, fill)
            self._win.draw_line(line2, fill)

        # up
        elif self._y1 > to_cell._y1:
            line1 = Line(Point(x_s, y_s), Point(x_s, self._y1))
            line2 = Line(Point(x_t, y_t), Point(x_t, to_cell._y2))
            self._win.draw_line(line1, fill)
            self._win.draw_line(line2, fill)

        # down
        elif self._y1 > to_cell._y1:
            line1 = Line(Point(x_s, y_s), Point(x_s, self._y2))
            line2 = Line(Point(x_t, y_t), Point(x_t, to_cell._y1))
            self._win.draw_line(line1, fill)
            self._win.draw_line(line2, fill)