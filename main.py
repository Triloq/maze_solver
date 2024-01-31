from graphics import Window, Line, Point

def main():
    win = Window(800, 600)
    point1,point2 = Point(500,500), Point(750,750)
    point3, point4 = Point(0,0), Point(800, 600)
    line1 = Line(point1, point2)
    line2 = Line(point3, point4)
    win.draw_line(line1, 'green')
    win.draw_line(line2, 'red')
    win.wait_for_close()

main()