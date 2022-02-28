"""
Name: <Evie Purcell>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""


def name_reverse():
    name = (input("enter a name (first last): "))
    x = name.split()
    first_name = x[0]
    last_name = x[1]
    print(last_name, ",", first_name)


def company_name():
    company = (input("enter company name with a three part domain: "))
    word = company.split(".")
    print(word[1], end="")

def initials():
    num_students = eval(input("how many students are in the class "))
    for i in range(num_students):
        f_name = input("enter students first name: ")
        l_name = input("enter students last name: ")
        print("initials:", f_name[0] + l_name[0])


def names():
    name = eval(input("enter a list of names, separated by commas: "))
    name_list = name.split(',')
    print("initials:", end=" ")
    for i in name_list:
        initial = i.split(" ")
        print(initial[0][0]+initial[1][0], end=" ")


def thirds():
    number = eval(input('enter number of sentences: '))
    sentence = []
    for i in range(number):
        sentences = input("enter sentence " + str(i + 1) + ": ")
        sentence.append(sentences)
    for i in sentence:
        output = ""
        for j in range(0, len(i), 3):
            output = output + i[j:j+1]
        print(output)
        output = ""

def word_average():
    total = 0
    word = input("enter a sentence:")
    x = word.split()
    number = len(x)
    for i in x:
        total = total + len(i)
    average = total / number
    print(average)

def pig_latin():
    sentence = eval(input("enter a sentence to convert to pig latin: "))
    word = sentence.split()
    new = ""
    for i in word:
        new += i[1:]+i[0]+"ay"
        new = new.lower()
        print(new)
pig_latin()

if __name__ == '__main__':

