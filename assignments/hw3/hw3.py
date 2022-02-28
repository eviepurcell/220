"""
Name: <Evie Purcell>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""


def average():
    num_of_grades = eval(input("How many grades will you enter? "))
    total_grades = 0
    for i in range(1, num_of_grades + 1):
        grades = eval(input("Enter grade: "))
        total_grades = total_grades + grades
        average = total_grades / num_of_grades
    print("average is", average)


def tip_jar():
    turns = 5
    donationtotal = 0
    for i in range(1, turns + 1):
        donationamount = eval(input("How much would you like to donate? "))
        donationtotal += donationamount
    print("Total tips: ", donationtotal)


def newton():
    x = int(input("What number do you want to square root? "))
    num_guess = int(input("How many times should we improve the approximation? "))
    initial = x
    for i in range(num_guess):
        initial = (initial + (x / initial)) / 2
    print("the square root is appromiately", initial)


def sequence():
    terms = eval(input("how many terms would you like? "))
    for i in range(1, terms + 1):
        termsquence = (i % 2) - 1 + i
        print(termsquence," ", end="")

def pi():
    term = eval(input("how many terms in the series? "))
    accum_term = 1
    for i in range(term):
        numerate = ((i + 1) % 2) + 1 + i
        demoninator = (i % 2) + (i + 1)
        accum_term *= numerate / demoninator
    print(2 * accum_term)

if __name__ == '__main__':
    pass
