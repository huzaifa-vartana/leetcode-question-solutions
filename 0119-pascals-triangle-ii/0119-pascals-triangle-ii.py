class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        prev_row = [1]
        for row_ptr in range(1, rowIndex + 1):
            curr_row = [0] * (row_ptr + 1)
            for col in range(row_ptr+1):
                left_ele = 0
                if col-1 in range(0, len(prev_row)):
                    left_ele = prev_row[col-1]

                right_ele = 0
                if col in range(0, len(prev_row)):
                    right_ele = prev_row[col]

                curr_row[col] = left_ele + right_ele

            prev_row = curr_row

        return prev_row