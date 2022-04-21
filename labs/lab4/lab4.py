from graphics import *

def greeting_card():
    win = GraphWin("Valentine's Day Greeting Card", 500, 500)
    win.setCoords(0.0, 0.0, 10.0, 10.0)

    # make arrow
    Arrow = Line(Point(-6.0, -6.0), Point(0.0, 0.5))
    Arrow.setArrow("last")
    Arrow.draw(win)

    # make the heart
    heart = Polygon(Point(2.0, 6.8), Point(3.5, 9.0), Point(5.0, 6.8), Point(6.5, 9.0), Point(8.0, 6.8), Point(5.0, 1.0))
    heart.draw(win)
    heart.setOutline("red")
    heart.setFill("pink2")

    # message on heart
    message = Text(Point(5.0, 6.0), "Happy Valentine's Day! <3")
    message.setFace("arial")
    message.setTextColor("red")
    message.draw(win)


    # move the arrow through the heart
    for i in range(40):
        i = Arrow.move(0.5, 0.5)
        time.sleep(0.1)

    # close window
    message = Text(Point(5.0, 0.5), "Click anywhere to close.")
    message.draw(win)

    win.getMouse()
    win.close()

greeting_card()


