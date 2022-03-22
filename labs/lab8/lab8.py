from graphics import *
from random import randint
import math

def get_random(move_amount):
    return randint(-move_amount, move_amount)

def did_collide(ball_1, ball_2):

    ball_1_radius = ball_1.getRadius()
    ball_2_radius = ball_2.getRadius()
    ball_1_x = ball_1.getCenter().getX()
    ball_2_x = ball_2.getCenter().getX()
    ball_1_y = ball_1.getCenter().getY()
    ball_2_y = ball_2.getCenter().getY()
    distance = math.sqrt((ball_1_x - ball_2_x) ** 2 + (ball_1_y - ball_2_y) ** 2)

    if (ball_1_radius + ball_2_radius) >= distance:
        return True
    else:
        return False

def hit_vertical(ball_1, win):

    radius_1 = ball_1.getRadius()
    center_1 = ball_1.getCenter().getY()
    height = win.getHeight()

    if (center_1 + radius_1) >= height:
        return True

    if (center_1 - radius_1) <= 0:
        return True


def hit_horizontal(ball_1, win):
    radius_2 = ball_1.getRadius()
    center_2 = ball_1.getCenter().getX()
    width = win.getWidth()

    if (radius_2 + center_2) >= width:
        return True

    if (center_2 - radius_2) <= 0:
        return True

def get_random_color():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 225)
    color = color_rgb(red, green, blue)

    return color

def bumper():
    win_width = 400
    win_height = 400
    win = GraphWin("bumper cars", win_width, win_height)
    circle_1 = Circle(Point(randint(1, 400), randint(1, 300)), 20)
    circle_1.setFill(get_random_color())
    circle_1.draw(win)
    circle_2 = Circle(Point(randint(1, 400), randint(1, 300)), 20)
    circle_2.setFill(get_random_color())
    circle_2.draw(win)

    circle_1_x_move = get_random(10)
    circle_2_x_move = get_random(10)
    circle_1_y_move = get_random(10)
    circle_2_y_move = get_random(10)

    while not win.checkMouse():
        circle_1.move(circle_1_x_move, circle_1_y_move)
        circle_2.move(circle_2_x_move, circle_2_y_move)

        if did_collide(circle_1, circle_2):
            circle_1_x_move = - circle_1_x_move
            circle_1_y_move = - circle_1_y_move
            circle_2_x_move = - circle_2_x_move
            circle_2_y_move = - circle_2_y_move

        if hit_vertical(circle_1, win):
            circle_1_y_move = - circle_1_x_move

        if hit_vertical(circle_2, win):
            circle_2_y_move = - circle_2_x_move

        if hit_horizontal(circle_1, win):
            circle_1_x_move = - circle_1_x_move

        if hit_horizontal(circle_2, win):
            circle_2_x_move = - circle_2_x_move


    win.close()


bumper()
