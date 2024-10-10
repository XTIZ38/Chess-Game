import os
import shutil
from echiquier import *
from pieces import *



def gameloop(board):
    while True:

        print(f"                                           C'est au tour des {board.current_turn}s. \n \n \n")
        board.display()
        try:
            start_row, start_col = map(int, input("\n \n Quelle piece bouge ? (ligne colonne): ").split())
            end_row, end_col = map(int, input("Ou va-t-elle ? (ligne colonne): ").split())
        except ValueError:
            print("Moi de base je comprends que les chiffres hein, je suis un ordinateur, mais je peux comprendre les paires de chiffres allant de 0 a 7")
            continue

        if board.move_piece((start_row, start_col), (end_row, end_col)):
            if board.is_checkmate(board.current_turn):
                board.display()
                print(f"Échec et mat ! {board.current_turn} a perdu.")
                break


def main():
    board = Board()
    board.display()
    gameloop(board)