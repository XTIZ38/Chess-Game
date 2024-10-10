import shutil
from pieces import *

class Board:
    def __init__(self):
        self.board = self.create_board()
        self.current_turn = 'blanc'

    def create_board(self):
        board = [[None] * 8 for i in range(8)]
        for i in range(8):
            board[1][i] = Pawn('blanc')
            board[6][i] = Pawn('nwar')

        board[0][0] = board[0][7] = Rook('blanc')
        board[7][0] = board[7][7] = Rook('nwar')

        board[0][1] = board[0][6] = Knight('blanc')
        board[7][1] = board[7][6] = Knight('nwar')

        board[0][2] = board[0][5] = Bishop('blanc')
        board[7][2] = board[7][5] = Bishop('nwar')

        board[0][3] = Queen('blanc')
        board[7][3] = Queen('nwar')

        board[0][4] = King('blanc')
        board[7][4] = King('nwar')

        return board

    def display(self):
        terminal_width = shutil.get_terminal_size().columns
        board_width = 19
        padding = (terminal_width - board_width) // 2

        print(" " * padding + "  0 1 2 3 4 5 6 7")
        for i, row in enumerate(self.board):
            row_str = " ".join([str(piece) if piece else '.' for piece in row])
            print(" " * padding + f"{i} {row_str} {i}")
        print(" " * padding + "  0 1 2 3 4 5 6 7")

    def move_piece(self, start, end):
        start_row, start_col = start
        end_row, end_col = end

        piece = self.board[start_row][start_col]
        if piece is None:
            print("Euuuh, je sais pas trop ce que t'as essayé de faire mais y'a aucune piece ici :)")
            return False
        if piece.color != self.current_turn:
            print(f"Ce n'est pas le tour des {piece.color}s.")
            return False
        if not piece.can_move(start, end, self.board):
            print(f"Raté {piece}, réessaie")
            return False
        if self.board[end_row][end_col] and self.board[end_row][end_col].color == piece.color:
            print("tu ne peux pas capturer tes propres pieces \U0001F480")
            return False

        temp = self.board[end_row][end_col]
        self.board[end_row][end_col] = piece
        self.board[start_row][start_col] = None

        if self.is_in_check(self.current_turn):
            self.board[start_row][start_col] = piece
            self.board[end_row][end_col] = temp
            print("Ca serai bete de se mettre tout seul en echec, non ?")
            return False

        self.current_turn = 'nwar' if self.current_turn == 'blanc' else 'blanc'
        return True

    def is_in_check(self, color):
        king_position = None
        for i in range(8):
            for j in range(8):
                if isinstance(self.board[i][j], King) and self.board[i][j].color == color:
                    king_position = (i, j)
                    break

        if king_position is None:
            raise ValueError(f"Le roi {color} n'a pas été trouvé sur l'échiquier")

        for i in range(8):
            for j in range(8):
                piece = self.board[i][j]
                if piece and piece.color != color and piece.can_move((i, j), king_position, self.board):
                    return True

        return False

        for i in range(8):
            for j in range(8):
                piece = self.board[i][j]
                if piece and piece.color != color and piece.can_move((i, j), king_position, self.board):
                    return True

        return False

    def is_checkmate(self, color):
        if not self.is_in_check(color):
            return False

        for i in range(8):
            for j in range(8):
                piece = self.board[i][j]
                if piece and piece.color == color:
                    for x in range(8):
                        for y in range(8):
                            start = (i, j)
                            end = (x, y)
                            if piece.can_move(start, end, self.board):
                                temp_piece = self.board[x][y]
                                self.board[x][y] = piece
                                self.board[i][j] = None
                                if not self.is_in_check(color):
                                    self.board[i][j] = piece
                                    self.board[x][y] = temp_piece
                                    return False
                                self.board[i][j] = piece
                                self.board[x][y] = temp_piece
        return True
