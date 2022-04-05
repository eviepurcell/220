from graphics import *

class Door:

    def __init__(self, shape, label):
        self.shape = shape
        self.text = Text(shape.getCenter(), label)

    def get_label(self):
        return self.text.getText()

    def set_label(self, label):
        self.text.setText(label)

    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self, point):
        xRange = (self.shape.getP1().getX() <= point.getX() and point.getX() and point.getX() <= self.shape.getP2.getX())
        yRange = (self.shape.getP2().getY() <= point.getY() and point.getY() and point.getY() <= self.shape.getP2.getY())
        return xRange and yRange

    def open(color, label):
        self.shape.setFill(color)
        self.text.setText(label)

    def close(color, label):
        self.shape.setFill(color)
        self.text.setText(label)

    def color_door(color):
        self.shape.setFill(color)

    def is_secret(self):
        return self.secret

    def set_secret(secret):
        self.secret = secret
