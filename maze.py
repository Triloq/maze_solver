from cell import Cell
import time
import random

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
            seed = None
        ):
        self._cells = None
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        if seed:
            self.seed = random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()     
        self._break_walls_r(0,0)   
        self._cells[len(self._cells)//2][len(self._cells[0])//2].visited = True
        self._reset_cells_visited()
        
    def _create_cells(self):
            self._cells = [[Cell(self.win) for _ in range(self.num_rows)] for _ in range(self.num_cols)]
            for i in range(0, self.num_cols):
                for j in range(0, self.num_rows):
                    self._draw_cells(i, j)     

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
        
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        m, n = len(self._cells)-1, len(self._cells[0])-1
        while True:
            to_vis = [] 
            right, left, up, down = True, True, True, True          
            if i == 0:
                right = self._cells[i+1][j].visited
            elif i == m:
                left = self._cells[i-1][j].visited
            else:
                left = self._cells[i-1][j].visited
                right = self._cells[i+1][j].visited

            if j == 0:
                down = self._cells[i][j+1].visited
            elif j == n:
                up = self._cells[i][j-1].visited
            else:
                up = self._cells[i][j-1].visited
                down = self._cells[i][j+1].visited

            if right == False:
                to_vis.append('right')
            if left == False:
                to_vis.append('left')
            if up == False:
                to_vis.append('up')
            if down == False:
                to_vis.append('down')

            if to_vis == []:
                self._draw_cells(i, j)
                return

            direction = random.choice(to_vis)

            if direction == 'right':
                self._cells[i][j].has_right_wall = False
                self._cells[i+1][j].has_left_wall = False
                self._break_walls_r(i+1,j)
            if direction == 'left':
                self._cells[i][j].has_left_wall = False
                self._cells[i-1][j].has_right_wall = False
                self._break_walls_r(i-1,j)
            if direction == 'up':
                self._cells[i][j].has_top_wall = False
                self._cells[i][j-1].has_bottom_wall = False
                self._break_walls_r(i,j-1)
            if direction == 'down':
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j+1].has_top_wall = False
                self._break_walls_r(i,j+1)
            
    def _reset_cells_visited(self):
        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._cells[i][j].visited = False

    def solve(self):
        return self._solve_r()

    def _solve_r(self, i=0, j=0):
    
        m, n = len(self._cells)-1, len(self._cells[0])-1
        self._animate()
        self._cells[i][j].visited = True

        if self._cells[i][j] == self._cells[m][n]:
            return True
        
        if self._can_go_to(i+1,j, 'right'):
            self._cells[i][j].draw_move(self._cells[i+1][j])
            if self._solve_r(i+1,j):
                return True
            self._cells[i][j].draw_move(self._cells[i+1][j], undo=True)
        if self._can_go_to(i-1,j, 'left'):
            self._cells[i][j].draw_move(self._cells[i-1][j])
            if self._solve_r(i-1,j):
                return True
            self._cells[i][j].draw_move(self._cells[i-1][j], undo=True)
        if self._can_go_to(i,j+1, 'down'):
            self._cells[i][j].draw_move(self._cells[i][j+1])
            if self._solve_r(i,j+1):
                return True
            self._cells[i][j].draw_move(self._cells[i][j+1], undo=True)
        if self._can_go_to(i,j-1, 'up'):
            self._cells[i][j].draw_move(self._cells[i][j-1])
            if self._solve_r(i,j-1):
                return True
            self._cells[i][j].draw_move(self._cells[i][j-1], undo=True)        
        return False

    def _can_go_to(self, i, j, direction):
        if i < 0 or i > len(self._cells)-1 or j < 0 or j > len(self._cells[0])-1:
            # cell is out of bounds
            return False
        elif self._cells[i][j].visited:
            # cell has been visited already
            return False 
        
        if direction == 'right' and self._cells[i][j].has_left_wall:
            return False
        if direction == 'left' and self._cells[i][j].has_right_wall:
            return False
        if direction == 'up' and self._cells[i][j].has_bottom_wall:
            return False
        if direction == 'down' and self._cells[i][j].has_top_wall:
            return False
        return True