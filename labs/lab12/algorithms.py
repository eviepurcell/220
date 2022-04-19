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



if __name__ == '__main__':

