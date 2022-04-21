from graphics import *
import math

def color_shape():

    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

  
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

   
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")

  
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")


    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")

    
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    
    win.getMouse()
    win.close()

def triange():
    win = GraphWin('Draw a Triangle', 1000, 700)
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5.0, 8.5), 'Plot the points for a triangle')
    message.draw(win)

    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)
    triangle = Polygon(p1, p2, p3)
    triangle.draw(win)

    # line lengths
    dx_a = abs(p1.getX() - p2.getX())
    dy_a = abs(p1.getY() - p2.getY())
    dx_b = abs(p2.getX() - p3.getX())
    dy_b = abs(p2.getY() - p3.getY())
    dx_c = abs(p3.getX() - p1.getX())
    dy_c = abs(p3.getY() - p1.getY())
    side_a = math.sqrt((dx_a * dx_a) + (dy_a * dy_a))
    side_b = math.sqrt((dx_b * dx_b) + (dy_b * dy_b))
    side_c = math.sqrt((dx_c * dx_c) + (dy_c * dy_c))

    perimeter = side_a + side_b + side_c
    perimeter_message = Text(Point(5.0, 1.5), 'Perimeter: ')
    per_measure = Text(Point(5.7, 1.5), float(round(perimeter, 2)))
    perimeter_message.draw(win)
    per_measure.draw(win)

    
    s = perimeter / 2
    area = math.sqrt(s * (s - side_a) * (s - side_b) * (s - side_c))
    area_message = Text(Point(5.0, 1.25), 'Area: ')
    area_measure = Text(Point(5.4, 1.25), float(round(area, 2)))
    area_message.draw(win)
    area_measure.draw(win)

    final_message = Text(Point(5.0, 0.5), 'Click anywhere to close.')
    final_message.draw(win)
    win.getMouse()
    win.close()

def color_shape_2():
    win = GraphWin('Color Shape', 1000, 700)
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    intro_message = Text(Point(5.0, 8.0), 'Draw the circle and color the shape five times.')
    intro_message.draw(win)

    
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    dx_a = abs(p1.getX() - p2.getX())
    dy_a = abs(p1.getY() - p2.getY())
    radius = math.sqrt((dx_a * dx_a) + (dy_a * dy_a))
    circle = Circle(p1, radius)
    circle.draw(win)

    red_message = Text(Point(3.5, 2.0), 'Red (0-255): ')
    blue_message = Text(Point(5.0, 2.0), 'Blue (0-255): ')
    green_message = Text(Point(6.5, 2.0), 'Green (0-255): ')
    red_entry = Entry(Point(3.5, 1.5), 3)
    blue_entry = Entry(Point(5.0, 1.5), 3)
    green_entry = Entry(Point(6.5, 1.5), 3)
    red_entry.draw(win)
    blue_entry.draw(win)
    green_entry.draw(win)
    red_message.draw(win)
    blue_message.draw(win)
    green_message.draw(win)

    for color_time in range(5):
        win.getMouse()
        red_color = int(red_entry.getText())
        green_color = int(green_entry.getText())
        blue_color = int(blue_entry.getText())
        circle.setFill(color_rgb(red_color, green_color, blue_color))
        repeat_message = Text(Point(5.0, 1.25), 'Click to change the color of the circle.')
        repeat_message.draw(win)


    final_message = Text(Point(5.0, 1.0), 'Click anywhere to close.')
    final_message.draw(win)
    win.getMouse()
    win.close()
color_shape_2()

def process_string():
    input_str = input("Input a string: ")
    first_chr = input_str[0]
    last_chr = input_str[-1]
    inclusive = input_str[1:4]
    first_three = input_str[0:3] * 10

    print(first_chr)
    print(last_chr)
    print(inclusive)
    print(first_three)
    for each_letter in input_str[:]:
        print(each_letter, end="\n")
    print(len(input_str))

def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    print(values[1]+values[3])
    print(values[0] + values[2])
    print(values[1] * 5)
    print(values[2:5])
    new_value = float(values[-1])
    print([values[2], values[0], new_value])
    print(values[0] + values[2] + new_value)
    print(len(values))

def another_series():
    terms_num = eval(input("Number of terms: "))
    values = [2, 4, 6]
    sum_of_nums = 0
    for num_2 in range(0, terms_num + 1, 3):
        num_2 = values[0]
        for num_4 in range(1, terms_num + 1, 3):
            num_4 = values[1]
            for num_6 in range(2, terms_num + 1, 3):
                num_6 = values[2]
                print(num_2, num_4, num_6)

def target():
    win = GraphWin("Target", 700, 700)
    win.setCoords(0.0, 0.0, 10.0, 10.0)


    circle_5 = Circle(Point(5.0, 5.0), 3.75)
    circle_5.setOutline('black')
    circle_5.setFill('white')
    circle_5.draw(win)
    circle_4 = Circle(Point(5.0, 5.0), 3.0)
    circle_4.setOutline('black')
    circle_4.setFill('black')
    circle_4.draw(win)
    circle_3 = Circle(Point(5.0, 5.0), 2.25)
    circle_3.setOutline('black')
    circle_3.setFill('blue')
    circle_3.draw(win)
    circle_2 = Circle(Point(5.0, 5.0), 1.5)
    circle_2.setOutline('black')
    circle_2.setFill('red')
    circle_2.draw(win)
    center_circle = Circle(Point(5.0, 5.0), 0.75)
    center_circle.setOutline('black')
    center_circle.setFill('yellow')
    center_circle.draw(win)

    message = Text(Point(5.0, 0.5), 'Click anywhere to close.')
    message.draw(win)
    win.getMouse()
    win.close()
