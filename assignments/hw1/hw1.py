"""
Name: <Evie Purcell>
<ProgramName>.py

Problem: In this exercise we used functions to do simple math like produce percentages, showing area, and convert
units of measure.

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)

def calc_volume():
    length = eval(input("Enter the Length: "))
    width = eval(input("Enter the Width: "))
    height = eval(input("Enter the Height: "))
    area = length * width * height
    print("Volume =", area)

def shooting_percentage():
    totalshot = eval(input("Enter the player's total shots: "))
    shots = eval(input("Enter how many shots the player made: "))
    total = (shots / totalshot) * 100
    print(("Shooting Percentage: ", total) + '%')

def coffee():
    pound = eval(input("How many pounds of coffee would you like?"))
    total = (10.50 * pound) + (.86 * pound) + 1.50
    print("You're total is:", total)

def kilometers_to_miles():
    kilometers = eval(input("How many kilometers did you travel? "))
    milestraveled = kilometers / 1.61
    print("That's", milestraveled, "miles")

if __name__ == '__main__':




