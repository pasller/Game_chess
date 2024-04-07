from src.piece import Piece


class Rook(Piece):
    def char(self):
        return 'R'

    def can_move(self, board, row: int, col: int, row_1: int, col_1: int) -> bool:
        return row == row_1 or col == col_1

    def can_attack(self, board, row: int, col: int, row_1: int, col_1: int) -> bool:
        return self.can_move(board, row, col, row_1, col_1)