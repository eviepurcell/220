def read_data(filename):
    file = open(filename, 'r')
    text = file.read()
    text = text.replace("\n", " ")
    text = text.split(" ")
    i = 0
    while i < len(text):
        text[i] = eval(text[i])
        i += 1
    return text


def is_in_linear(search_val, values):
    i = 0
    while i < len(search_val) and search_val != values:
        i += 1
    return i < len(search_val)

def is_in_binary(search_val, values):
    low = 0
    high = len(values) - 1
    mid = 0
    while low <= high:

        mid = (high + low) // 2

        if values[mid] < search_val:
            low = mid + 1
        elif values[mid] > search_val:
            high = mid - 1
        else:
            return True
    return False

def good_input():
    user = eval(input("The range is 1-10. Input within range: "))
    while user < 1 or user > 10:
        if user < 1:
            print("Input was too low")
        else:
            print("Input was too high")
        user = eval(input("Try again:"))
    return user



def num_digits():
    inputuser = eval(input("Insert positive number (enter 0 or a negative to end program): "))
    while inputuser > 0:
        count = 0
        while inputuser > 0:
            inputuser = inputuser // 10
            count = count + 1
        print("this number contains", count, "digits")
        inputuser = eval(input("enter a positive number: "))

def hi_lo_game():
    randomnumber = randint(1, 100)
    accguesses = 7
    user_guess = eval(input("guess number: "))
    accguesses = accguesses - 1
    while accguesses != 0 and accguesses != -1:
        if user_guess > randomnumber:
            user_guess = eval(input("Guess is too high, try again: "))
            accguesses = accguesses - 1
        if user_guess < randomnumber:
            user_guess = eval(input("Guess is too low, try again: "))
            accguesses = accguesses - 1
        if user_guess == randomnumber:
            print("You won in", 7 - user_guess, "guesses!")
            guesses = -1
    if guesses == 0:
        print("You've lost! The number was", randomnumber)

def selection_sort(values):
    n = len(values)
    for j in range(n):
        mp = j
        for i in range(j, n):
            if values[i] < values[mp]:
                mp = i
        values[j], values[mp] = values[mp], values[j]

def rect_sort(rectangles):
    amount = len(rectangles)
    for least in range(amount - 1):
        mp = least
        for i in range(least, n):
            if calc_area(rectangles[i]) < calc_area(rectangles[mp]):
                mp = i
        rectangles[least], rectangles[mp] = rectangles[mp], rectangles[least]


def calc_area(rect):
    y1 = rect.getP1().getY()
    y2 = rect.getP2().getY()
    x1 = rect.getP1().getX()
    x2 = rect.getP2().getX()
    length = abs(y2 - y1)
    width = abs(x2 - x1)
    area = length * width
    return area







if __name__ == '__main__':
    test_list = [7, 4, 6, 2, 3, 1]
    print(test_list)
    selection_sort(test_list)
    print(test_list)