from graphics import Window
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 600)

    # cell1 = Cell(win)
    # cell1.draw(200, 200, 250, 250)
    # cell2 = Cell(win)
    # cell2.draw(400, 400, 500, 500)
    # cell2.draw_move(cell1, undo=True)

    # win.wait_for_close()

    maze = Maze(100, 100, 20, 20, 30, 30, win)
    win.wait_for_close()
    

main()







#     cell1 = Cell(point1, point2, win)
#     cell1.draw()
#     cell2 = Cell(point3, point4, win)
#     cell2.draw()

    # line1 = Line(point1, point2)
    # line2 = Line(point3, point4)
    # win.draw_line(line1, 'green')
    # win.draw_line(line2, 'red')