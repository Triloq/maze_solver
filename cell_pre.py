from graphics import Line, Point

class Cell():
    def __init__(self, top_left_corner, bottom_right_corner, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = top_left_corner.x
        self._x2 = bottom_right_corner.x
        self._y1 = top_left_corner.y
        self._y2 = bottom_right_corner.y
        self._win = window

    def draw(self):
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
        line = Line(Point(x_s, y_s), Point(x_t, y_t))
        if undo == False:
            self._win.draw_line(line, 'red')
        elif undo:
            self._win.draw_line(line, 'gray')