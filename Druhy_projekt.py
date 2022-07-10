import random

separator = 42 * ("=")

print("Weclome to Tic Tac Toe")
print(separator)
print("""GAME RULES:
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or
* diagonal row""")
print(separator)
print("Let's start the game")
print(separator)

board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]

current_player = "X"
winner = None
game_running = True

# game board
def print_board(board):
    print("+---+---+---+")
    print("|" + board[0] + "|" + board[1] + "|" + board[2] + "|")
    print("+---+---+---+")
    print("|" + board[3] + "|" + board[4] + "|" + board[5] + "|")
    print("+---+---+---+")
    print("|" + board[6] + "|" + board[7] + "|" + board[8] + "|")
    print("+---+---+---+")




def player_input(board):
    print(separator)
    try:
        pl_inp = int((input("Choose spot 1-9: ")))
        print("You have to enter just numbers 1 - 9!!")
        print(separator)
        if board[pl_inp-1] == " ":
            board[pl_inp-1] = current_player
    except ValueError:
            print("You must enter number 1-9! Closing app, start again with number.")
            quit()
    else:
        print("This spot has been already taken.")



def check_horizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != " ":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != " ":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != " ":
        winner = board[6]
        return True

def check_rows(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != " ":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != " ":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != " ":
        winner = board[3]
        return True


def check_diagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != " ":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[4] != " ":
        winner = board[2]
        return True


def check_win(board):
    global game_running
    if check_horizontal(board):
        print_board(board)
        print(f"Congratulations, the player {winner} won!")
        game_running = False

    elif check_rows(board):
        print_board(board)
        print(f"Congratulations, the player {winner} won!")
        game_running = False

    elif check_diagonal(board):
        print_board(board)
        print(f"Congratulations, the player {winner} won!")
        game_running = False


def check_tie(board):
    global game_running
    if " " not in board:
        print_board(board)
        print("It is a tie!")
        game_running = False

def change_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"


def computer(board):
    while current_player == "O":
        position = random.randint(0, 8)
        if board[position] == " ":
            board[position] = "O"
            change_player()


while game_running:
    print_board(board)
    player_input(board)
    check_win(board)
    check_tie(board)
    change_player()
    computer(board)
    check_win(board)
    check_tie(board)
