class Solution:
    def minDistance(self, s: str, t: str) -> int:
        
        
        l1, l2 = len(s), len(t)

        cache = [[float('inf') for _ in range(l2+1)] for _ in range(l1+1)]
        cache[l1][l2] = 0
        for i in range(l2): cache[l1][i] = l2 - i
        for j in range(l1): cache[j][l2] = l1 - j
        for i in range(l1-1, -1, -1):
            for j in range(l2-1, -1, -1):

                count = float('inf')
                if s[i] == t[j]: count = min(count, cache[i+1][j+1])
                else:
                    replace = 1 + cache[i+1][j+1]
                    delete = 1 + cache[i+1][j]
                    insert = 1 + cache[i][j+1]

                    count = min(delete, insert, replace)


                cache[i][j] = count



        return cache[0][0]
    
    
#             def solve(i, j):

#             if i >= l1 and j >= l2: return 0
#             if i >= l1: return l2 - j
#             if j >= l2: return l1 - i