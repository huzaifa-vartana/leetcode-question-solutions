class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Check each 3x3 grid
        squares = collections.defaultdict(set)
        row = collections.defaultdict(set)
        col = collections.defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in row[i] or board[i][j] in col[j] or board[i][j] in squares[(i//3, j//3)]:
                        return False
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                    squares[(i//3, j//3)].add(board[i][j])

        return True
