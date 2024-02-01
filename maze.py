from cell import Cell
import time

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
        ):
        self._cells = None
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win

    def _create_cells(self):
        self._cells = [[Cell(self.win)]*self.num_rows for i in range(0, self.num_cols)]
        for i in range(0, self.num_cols):
            for j in range(0, self.num_rows):
                self._draw_cells(i, j)            

    def _draw_cells(self, i, j):
        x1 = self.x1 + self.cell_size_x*i 
        y1 = self.y1 + self.cell_size_y*j
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        print(f'{x1},{y1} : {x2},{y2}')
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        self.win.redraw()
        time.sleep(0.1)