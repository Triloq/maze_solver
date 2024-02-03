from graphics import Window
from cell import Cell
from maze import Maze

def main():

    win = Window(800, 600)
    maze = Maze(100, 100, 20, 20, 30, 30, win)
    maze.solve()
    win.wait_for_close()

main()



