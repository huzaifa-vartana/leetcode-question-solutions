class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # validate rows
        for row in range(9):
            rows_set = set()
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] in rows_set:
                    print("rows validation")
                    print(f"row: {row}, col: {col}")
                    return False
                rows_set.add(board[row][col])

        # validate columns
        for col in range(9):
            cols_set = set()
            for row in range(9):
                if board[row][col] == ".":
                    continue

                if board[row][col] in cols_set:
                    print("cols validation")
                    print(f"row: {row}, col: {col}")
                    return False

                cols_set.add(board[row][col])

        # validate squares
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                square_set = set()
                for i in range(3):
                    for j in range(3):
                        if board[row+i][col+j] == ".":
                            continue

                        if board[row+i][col+j] in square_set:
                            print("squares validation")
                            print(f"row: {row+i}, col: {col+j}")
                            return False

                        square_set.add(board[row+i][col+j])

        return True
