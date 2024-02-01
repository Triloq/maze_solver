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
        self._create_cells()
        
    def _create_cells(self):
            self._cells = [[Cell(self.win) for _ in range(self.num_rows)] for _ in range(self.num_cols)]
            for i in range(0, self.num_cols):
                for j in range(0, self.num_rows):
                    self._draw_cells(i, j)     
            self._break_entrance_and_exit()        

    def _draw_cells(self, i, j):
        x1 = self.x1 + self.cell_size_x*i 
        y1 = self.y1 + self.cell_size_y*j
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self.win is not None:
            self.win.redraw()
        # time.sleep(0.1)
            
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cells(0, 0)
            
        self._cells[self.num_cols-1][self.num_rows-1].has_bottom_wall = False
        self._draw_cells(self.num_cols-1, self.num_rows-1)
        