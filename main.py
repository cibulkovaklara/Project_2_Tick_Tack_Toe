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

