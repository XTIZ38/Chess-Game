from echiquier import *


class Piece:
    def __init__(self, color):
        self.color = color

    def can_move(self, start, end, board):
        """Chaque classe a des mouvements différents, donc on override la methode dans chaque sous classe"""
        raise NotImplementedError

    def __str__(self):
        return self.symbol


class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = '\u2659' if color == 'blanc' else '\u265F'

    def can_move(self, start, end, board):
        start_row, start_col = start[0], start[1]
        end_row, end_col = end[0], end[1]
        direction = 1 if self.color == 'blanc' else -1

        if start_col == end_col:
            if end_row == start_row + direction and board[end_row][end_col] is None:
                return True
            if (start_row == 1 or start_row == 6) and end_row == start_row + 2 * direction and board[end_row][end_col] is None:
                return True

        if abs(start_col - end_col) == 1 and end_row == start_row + direction:
            if board[end_row][end_col] and board[end_row][end_col].color != self.color:
                return True

        return False


class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = '\u2656' if color == 'blanc' else '\u265C'

    def can_move(self, start, end, board):
        start_row, start_col = start[0], start[1]
        end_row, end_col = end[0], end[1]
        if start_row == end_row or start_col == end_col:
            if Rook.path_is_clear(start, end, board):
                return True
        return False

    @staticmethod
    def path_is_clear(start, end, board):
        start_row, start_col = start
        end_row, end_col = end
        if start_row == end_row:
            step = 1 if start_col < end_col else -1
            for col in range(start_col + step, end_col, step):
                if board[start_row][col] is not None:
                    return False
        elif start_col == end_col:
            step = 1 if start_row < end_row else -1
            for row in range(start_row + step, end_row, step):
                if board[row][start_col] is not None:
                    return False
        return True


class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = '\u2658' if color == 'blanc' else '\u265E'

    def can_move(self, start, end, board):
        start_row, start_col = start[0], start[1]
        end_row, end_col = end[0], end[1]
        row_diff = abs(end_row - start_row)
        col_diff = abs(end_col - start_col)
        if (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2):
            if board[end_row][end_col] is None or board[end_row][end_col].color != self.color:
                return True
        return False


class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = '\u2657' if color == 'blanc' else '\u265D'

    def can_move(self, start, end, board):
        start_row, start_col = start[0], start[1]
        end_row, end_col = end[0], end[1]
        if abs(start_row - end_row) == abs(start_col - end_col):
            if Bishop.path_is_clear(start, end, board):
                return True
        return False

    @staticmethod
    def path_is_clear(start, end, board):
        start_row, start_col = start[0], start[1]
        end_row, end_col = end[0], end[1]
        step_row = 1 if start_row < end_row else -1
        step_col = 1 if start_col < end_col else -1
        row, col = start_row + step_row, start_col + step_col
        while row != end_row and col != end_col:
            if board[row][col] is not None:
                return False
            row += step_row
            col += step_col
        return True


class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = '\u2655' if color == 'blanc' else '\u265B'

    def can_move(self, start, end, board):
        return Rook.can_move(self, start, end, board) or Bishop.can_move(self, start, end, board)


class King(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = '\u2654' if color == 'blanc' else '\u265A'

    def can_move(self, start, end, board):
        start_row, start_col = start[0], start[1]
        end_row, end_col = end[0], end[1]
        if abs(start_row - end_row) <= 1 and abs(start_col - end_col) <= 1:
            if board[end_row][end_col] is None or board[end_row][end_col].color != self.color:
                return True
        return False
