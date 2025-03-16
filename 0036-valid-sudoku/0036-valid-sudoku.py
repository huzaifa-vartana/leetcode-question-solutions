class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = defaultdict(set)
        col_set = defaultdict(set)
        box_set = defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] == '.': continue
                if board[row][col] in row_set[row] or  board[row][col] in col_set[col] or board[row][col] in box_set[(row//3, col//3)]: return False

                row_set[row].add(board[row][col])
                col_set[col].add(board[row][col])
                box_set[(row//3, col//3)].add(board[row][col])


        return True


        