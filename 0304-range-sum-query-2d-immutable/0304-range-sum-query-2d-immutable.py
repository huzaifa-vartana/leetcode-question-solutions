class NumMatrix:

    def __init__(self, matrix: List[List[int]]):

        N, M = len(matrix), len(matrix[0])
        self.matrix_sum = [[0 for _ in range(M+1)] for _ in range(N+1)]
        
        for row in range(1, N+1):
            for col in range(1, M+1):
                left = self.matrix_sum[row][col-1]
                top = self.matrix_sum[row-1][col]
                diagonal = self.matrix_sum[row-1][col-1]

                self.matrix_sum[row][col] = matrix[row-1][col-1] + left + top - diagonal


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1 += 1
        row2 += 1
        col1 += 1
        col2 += 1

        return self.matrix_sum[row2][col2] - self.matrix_sum[row2][col1-1] - self.matrix_sum[row1-1][col2] + self.matrix_sum[row1-1][col1-1]
        
        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)