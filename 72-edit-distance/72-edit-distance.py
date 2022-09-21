class Solution:
    def minDistance(self, s: str, t: str) -> int:
        
        
        l1, l2 = len(s), len(t)

        cache = [[-1 for _ in range(l2+1)] for _ in range(l1+1)]
        def solve(i, j):

            if i >= l1 and j >= l2: return 0
            if cache[i][j] != -1: return cache[i][j]

            count = float('inf')
            if i < l1 and j < l2 and s[i] != t[j]:
                replace = 1 + solve(i+1, j+1)
                delete = 1 + solve(i+1, j)
                insert = 1 + solve(i, j+1)

                count = min(delete, insert, replace)

            elif i < l1 and j < l2 and s[i] == t[j]:
                count = min(count, solve(i+1, j+1))

            elif i < l1 and j >= l2:
                count = min(count, 1 + solve(i+1, j))

            elif i >= l1 and j < l2:
                count = min(count, 1 + solve(i, j+1))

            cache[i][j] = count
            return cache[i][j]


        return solve(0, 0)
        