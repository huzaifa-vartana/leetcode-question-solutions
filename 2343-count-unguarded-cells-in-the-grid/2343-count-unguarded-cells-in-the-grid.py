class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        """
        0 - unguarded
        1 - guard
        2 - wall
        3 - guarded
        """
        grid = [[0 for _ in range(n)] for _ in range(m)]
        
        for wx, wy in walls:
            grid[wx][wy] = 2
        for wx, wy in guards:
            grid[wx][wy] = 1

        for row, col in guards:
            for y in range(col-1, -1, -1):
                if grid[row][y] == 3: continue
                if grid[row][y] in [1, 2]: break
                grid[row][y] = 3

            # right row
            for y in range(col+1, n):
                if grid[row][y] == 3: continue
                if grid[row][y] in [1, 2]: break
                grid[row][y] = 3

            # cols fixed
            # upper row
            for x in range(row-1, -1, -1):
                if grid[x][col] == 3: continue
                if grid[x][col] in [1, 2]: break
                grid[x][col] = 3
            for x in range(row+1, m):
                if grid[x][col] == 3: continue
                if grid[x][col] in [1, 2]: break
                grid[x][col] = 3
        return sum(1 for i in range(m) for j in range(n) if grid[i][j] == 0)
        