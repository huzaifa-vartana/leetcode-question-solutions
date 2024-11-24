from collections import deque
from typing import List


class Solution:
    def snakesAndLadders(self, grid: List[List[int]]) -> int:
        N = len(grid)
        def valid(x, y): return x >= 0 and x < N and y >= 0 and y < M
        time = 0

        seen = set()
        q = deque([])
        q.append(1)
        seen.add(1)
        target = N * N

        def numToCoords(number):
            r, c = (number - 1) // N, (number - 1) % N
            c = c if r % 2 == 0 else ~c
            return [~r, c]

        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                for move in range(curr + 1, min(curr + 7, target+1)):
                    r, c = numToCoords(move)
                    x = move
                    if grid[r][c] != -1: x = grid[r][c]
                    if x == target: return time + 1
                    if x in seen: continue

                    q.append(x)
                    seen.add(x)

            time += 1

        return -1

