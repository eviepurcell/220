"""
Name: <evie purcell>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
"""
import math

def sum_of_threes():
    upperbound = int(input("what is the upper bound? "))
    for i in range(1, upperbound+1):
        print(upperbound*i, end="")

def multiplication_table():
    for i in range(1,11):
        for j in range(1,11):
          print(i * j, end='\t')
        print('')


def triangle_area():
    aside = eval(input("What is the length of A side?:"))
    bside = eval(input("What is the length of B side?:"))
    cside = eval(input("What is the length of C side?:"))
    side = (aside + bside + cside) / 2
    area = (math.sqrt(side(side - aside)(side - bside)(side - cside)))
    print("The area is:", area)
    triangle_area()


def sum_squares():
    my_sum = 0
    for i in range(3,5):
        my_sum = my_sum + (i * i)
    print(sum)


def power():
    base = eval(input("Enter the base number: "))
    exponent = eval(input("Enter the base exponent: "))
    my_sum = 1
    for i in range(exponent):
        my_sum = my_sum * base
    print("my_sum", my_sum)

sum_of_threes()
multiplication_table()
triangle_area()
sum_squares()
power()

if __name__ == '__main__':
