from src.piece import Piece


class Bishop(Piece):
    def char(self):
        return 'E'

    def can_move(self, board, row: int, col: int, row_1: int, col_1: int) -> bool:
        diff_row = abs(row - row_1)
        diff_col = abs(col - col_1)
        if diff_row != diff_col:
            return False

        step_row = 1 if row_1 > row else -1
        step_col = 1 if col_1 > col else -1

        cur_row, cur_col = row + step_row, col + step_col
        while cur_row != row_1 and cur_col != col_1:
            if board[cur_row][cur_col] is not None:
                return False
            cur_row += step_row
            cur_col += step_col

        return True

    def can_attack(self, board, row: int, col: int, row_1: int, col_1: int) -> bool:
        return self.can_move(board, row, col, row_1, col_1)
