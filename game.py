from echiquier import *


def gameloop(board):
    while True:
        board.display()
        start = input("Déplacez une pièce (format: ligne,colonne): ")
        end = input("Vers (format: ligne,colonne): ")

        start = tuple(map(int, start.split(',')))
        end = tuple(map(int, end.split(',')))

        if not board.move_piece(start, end):
            continue

        if board.is_checkmate(board.current_turn):
            print(f"Échec et mat ! Les {board.current_turn}s ont perdu.")
            break


def main():
    board = Board()
    gameloop(board)