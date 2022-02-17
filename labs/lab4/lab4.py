"""
Name: <your name goes here – first and last>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""

from graphics import *



def squares():
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("5", 400, 400)
    circles = Circle(Point(50,50), 20)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to move circle")
    instructions.draw(win)

    # builds a circle
    shape = Circle(Point(50, 50), 20)
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the circle
    for i in range(num_clicks):
        click = win.getMouse()
        center = shape.getCenter()  # center of circle

        # move amount is distance from center of circle to the
        # point where the user clicked
        change_x = click.getX() - center.getX()
        change_y = click.getY() - center.getY()
        shape.move(change_x, change_y)

    win.getMouse()
    win.close()


def rectangle():
    win = GraphWin("rectangle", 400, 400)
    text = Text(Point(200, 50))
    text = Text.setSize(10)
    text.draw(win)

    point_1 = win.getMouse()
    point_1.draw(win)
    point_2 = win.getMouse()
    point_1.undraw(win)
    draw = Rectangle(point_1, point_2)
    draw.draw(win)

    length = point_2.getX() - point_1.getY()
    width = point_2,getX() - point_2.getY()
    area = length * width
    perimeter = 2 * length * 2 * width
    text_1 = Text(Point(200,50), "Perimeter: ",)
    text_1.setSize(10)
    text_2 = Text(Point(200, 25), "Area: ")
    win.getMouse()

def circle():
    win = GraphWin("circle", 400, 400)
    center = win.getMouse()
    point = win.getMouse()
    circle_x = point.getX() - center.getY()
    circle_y = point.getY() - center.getY()
    formula = math.sgrt(circle_x ** 2 + circle_y ** 2)
    circle_1 = Circle(center, formula)
    circle_1.setFill("light blue")
    win.getMouse()
    win.close()

def pi2():
    import math
    n = input("number of terms to sum: ")
    n = int()
    pi = 0
    for pi in range(n):
        terms = ((-1 ** pi) * (2 * pi + 1))
        terms * pi

    print("pi approximation:", pi)
    print("accuracy:", math.pi - pi)
    pi2()


if __name__ == '__main__':
    rectangle()
    circle()
    squares()
    pi2()
