from lab10.door import Door
from lab10.button import Button
from graphics import *
from random import randint


def main():
    win = GraphWin('Three Door Game', 1000, 800)
    win.setCoords(0.0, 0.0, 10.0, 10.0)
#draw door one
    door_1 = Door(Rectangle(Point(1.0, 0.0), Point(3.0, 6.0)), 'Door 1')
    door_1.color_door('Saddle Brown')
    door_1.draw(win)

    door_2 = Door(Rectangle(Point(4.0, 0.0), Point(6.0, 6.0)), 'Door 2')
    door_2.color_door('Saddle Brown')
    door_2.draw(win)

    door_3 = Door(Rectangle(Point(7.0, 0.0), Point(9.0, 6.0)), 'Door 3')
    door_3.color_door('Saddle Brown')
    door_3.draw(win)


    quit_button = Button(Rectangle(Point(1.0, 7.5), Point(4.0, 9.5)), 'Quit')
    quit_button.draw(win)

    wins = 0
    scorebox1 = Rectangle(Point(6.0, 7.5), Point(7.0, 9.5))
    scorebox1.draw(win)
    wintext = Text(scorebox1.getCenter(), wins)
    wintext.draw(win)


    lose = 0
    scorebox2 = Rectangle(Point(7.0, 7.5), Point(8.0, 9.5))
    scorebox2.draw(win)
    losetext = Text(scorebox1.getCenter(), lose)
    losetext.draw(win)



    pt = win.getMouse()

    while not quit_button.is_clicked(pt):
        doors = [door_1, door_2, door_3]
        random_door = randint(0, len(doors) -1)
        #set_secret(door[random_door]) == True
        doors[random_door].set_secret(True)
        for door in doors:
            if door.is_clicked(pt) and door.is_secret():
                door.color_door('Green')  #when they pick the right one
                win += 1
                wintext.setText(str(wins))
                pt = win.getMouse()
            elif door.is_clicked(pt) and not door.is_secret():
                door.color_door('Red')  #when they pick the wrong one
                lose += 1
                losetext.setText(str(lose))
                pt = win.getMouse()
            elif not door.is_clicked(pt) and door.is_secret():
                door.color_door('Green')
                pt = win.getMouse()
        if quit_button.is_clicked(pt):
            break

        door.set_secret(False)
        door.color_door('Saddle Brown')
        pt = win.getMouse()

    win.getMouse()
    win.close()
main()
