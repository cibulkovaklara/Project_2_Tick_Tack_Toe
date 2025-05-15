"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Klara Cibulkova
email: cibulkovaklara@seznam.cz
"""
# přidání pro kompatibilitu s různými verzemi Pythonu
from typing import List

def welcome():
    """Zobrazí uvítací zprávu a pravidla hry."""
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

def create_board() -> List[str]:
    """Vytvoří a vrátí prázdnou hrací desku (seznam 9 políček)."""
    return [" " for _ in range(9)]

def print_board(board: List[str]):
    """Vytiskne aktuální stav hrací desky."""
    print("=" * 43)
    for i in range(3):
        print("+---+---+---+")
        print(f"| {board[i*3]} | {board[i*3+1]} | {board[i*3+2]} |")
    print("+---+---+---+")
    print("=" * 43)

def is_valid_move(board: List[str], move: int) -> bool:
    """Zkontroluje, zda je zadaný tah platný (tj. volné políčko)."""
    return board[move] == " "

def is_winner(board: List[str], player: str) -> bool:
    """Zkontroluje, zda daný hráč vyhrál hru."""
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8], # řádky
        [0,3,6], [1,4,7], [2,5,8], # sloupce
        [0,4,8], [2,4,6]           # diagonály
    ]
    return any(all(board[i] == player for i in condition) for condition in win_conditions)

def is_draw(board: List[str]) -> bool:
    """Zkontroluje, zda hra skončila remízou (všechna políčka obsazena)."""
    return all(cell != " " for cell in board)

def get_move(player: str, board: List[str]) -> int:
    """Získá a ověří tah hráče. Vrací index (0–8)."""
    while True:
        try:
            user_input = input(f"Player {player} | Please enter your move number (1-9): ")
            move = int(user_input) - 1  # Převod na index
            if move < 0 or move > 8:
                print("Invalid input. Please choose a number from 1 to 9.")
            elif not is_valid_move(board, move):
                print("This cell is already occupied. Choose another one.")
            else:
                return move
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def play_game():
    """Spustí hru Tic Tac Toe pro dva hráče."""
    welcome()
    board = create_board()
    current_player = "X" # Začíná hráč X

    while True:
        print_board(board)
        move = get_move(current_player, board)
        board[move] = current_player

        if is_winner(board, current_player):
            print_board(board)
            print(f"Congratulations, the player {current_player} WON!")
            break       
        elif is_draw(board):
            print_board(board)
            print("It's a DRAW!")
            break

        # Přepnutí hráče
        current_player = "0" if current_player == "X" else "X"

if __name__ == "__main__":
    play_game()

