class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        # two binary searches

        # first binary search to find the correct row number
        row = None
        l, r = 0, rows - 1
        while l <= r:
            m = (l+r) // 2
            if matrix[m][-1] >= target:
                r = m - 1
                row = m
            else: 
                l = m + 1
                


        if row not in range(rows): return False

        l, r = 0, cols - 1
        while l <= r:
            m = (l+r) // 2
            if matrix[row][m] == target:
                return True
            elif matrix[row][m] > target:
                r = m - 1
            else: 
                l = m + 1


        return False