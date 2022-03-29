"""
Name: <Evie Purcell>
<ProgramName>.py
"""


def build_board():
        board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        return board


def print_board(board):
    """ prints the values of baord """
    RED = "\033[1;31m"
    BLUE = "\033[1;36m"
    LIGHT_GRAY = "\033[0;37m"
    reset = "\033[0m"
    new_board = []
    for v in board:
        new_board.append(v)
    for i in range(len(board)):
        if str(board[i]).find('x') >= 0:
            new_board[i] = RED + board[i] + LIGHT_GRAY
        elif str(board[i]).find('o') >= 0:
            new_board[i] = BLUE + board[i] + LIGHT_GRAY
    row_format = ' {0} | {1} | {2} '
    row_1 = row_format.format(new_board[0], new_board[1], new_board[2])
    row_2 = row_format.format(new_board[3], new_board[4], new_board[5])
    row_3 = row_format.format(new_board[6], new_board[7], new_board[8])
    row_separator = '-' * 11
    print(LIGHT_GRAY)
    print(row_1)
    print(row_separator)
    print(row_2)
    print(row_separator)
    print(row_3)
    print(reset)

def is_legal(board, position):
    if board[position] == 'o' or board[position] == 'x' and 0 <= position >= 9:
        return False
    else:
        return True

def fill_spot(board, position, shape):
    shape = shape.strip().lower()
    board[position-1] = shape


def winning_game(board):
    for i in range(0, 8, 3):
        if board[i] == board[i+1] == board[i+2]:
            return True
    for i in range(0, 3, 1):
        if board[i] == board[i + 1] == board[i + 2]:
            return True
    if board[0] == board[4] == board[8]:
        return True
    if board[2] == board[4] == board[6]:
        return True
    else:
        return False

def game_over(board):
    tie = True
    for i in range(9):
        if board[i] != "x" or board[i] != "o":
            tie = False
        return winning_game(board) or tie

def get_winner(board):
    if winning_game(board):
        xCount = 0
        oCount = 0

        for position in board:
            if position == 'x':
                xCount += 1
            elif position == 'o':
                oCount += 1

        if xCount == oCount:
            return 'o'
        else:
            return 'x'

    else:
        return None

def play(board):
    x_turn = 0
    o_turn = 0
    while game_over(board) == False:
        print_board(board)
        if x_turn == o_turn:
            position = int(input("it's x's turn, enter position: "))
            if is_legal(board, position) == True:
                fill_spot(board, position, 'x')
                x_turn += 1
        else:
            position = int(input("it's o's turn, enter position: "))
            if is_legal(board, position) == True:
                fill_spot(board, position, 'o')
                o_turn += 1
    if winning_game(board) == True:
        print(get_winner(board))
    else:
        print("Tie")
    playagain = input("do you want to play again?")
    if playagain == "yes":
        newboard = build_board()
        play(newboard)

def main():
    pass


if __name__ == '__main__':
    main()
    playboard = build_board()
    play(playboard)

