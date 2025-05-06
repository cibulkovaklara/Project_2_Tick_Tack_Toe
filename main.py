"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Klara Cibulkova
email: cibulkovaklara@seznam.cz
"""

def welcome():
    print("Welcome to Tic Tac Toe")
    print("=" * 43)
    print("GAME RULES:")
    print("Each player can place one mark (or stone)")
    print("per turn on the 3x3 grid. The WINNER is")
    print("who succeeds in placing three of their")
    print("marks in a:\n* horizontal,\n* vertical or\n* diagonal row")
    print("=" * 43)
    print("Let's start the game")
    print("-" * 43)

#Funkce pro vytvoření prázdné hrací desky (9 políček)
def create_board():
    return [" " for _ in range(9)]

def print_board(board):
    print("=" * 43)
    for i in range(3):
        print("+---+---+---+")
        print(f"| {board[i*3]} | {board[i*3+1]} | {board[i*3+2]} |")
    print("+---+---+---+")
    print("=" * 43)

def is_valid_move(board, move):
    return board[move] == " "

def is_winner(board, player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    return any(all(board[i] == player for i in condition) for condition in win_conditions)

def is_draw(board):
    return all(cell != " " for cell in board)

def get_move(player, board):
    while True:
        try:
            move = int(input(f"Player {player} | Please enter your move number (1-9): "))
            if move < 1 or move > 9:
                print("Invalid input. Please choose a number from 1 to 9.")
            elif not is_valid_move(board, move - 1):
                print("This cell is already occupied. Choose another one.")
            else:
                return move - 1
        except ValueError:
            print("Invalid input. Please enter a number.")

def play_game():
    welcome()
    board = create_board()
    current_player = "O"

while True:
        print_board(board)
        move = get_move(current_player, board)
        board[move] = current_player

