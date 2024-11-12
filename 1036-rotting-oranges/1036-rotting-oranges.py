from queue import Queue
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0])
        q = []
        time, fresh, rotten = 0, 0, 0
        def valid(x, y): return x >= 0 and x < N and y >= 0 and y < M
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        for i in range(N):
            for j in range(M):
                if grid[i][j] == 2:
                    q.append((i, j))
                    rotten += 1
                if grid[i][j] == 1:
                    fresh += 1
        if rotten == 0 and fresh > 0: return -1
        if rotten == 0: return 0

        while q:
            for _ in range(len(q)):
                i, j = q.pop(0)
                pos = False
                for x, y in directions:
                    i_, j_ = i + x, j + y
                    if not valid(i_, j_) or grid[i_][j_] != 1:
                        continue
                    grid[i_][j_] = 2
                    q.append((i_, j_))
                    fresh -= 1
            time += 1

        return -1 if fresh > 0 else time - 1
