class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        
        n = len(piles)
        cache = [[-1 for _ in range(k+1)] for _ in range(n+1)]
        def solve(idx, picked):
            if picked > k: return float('-inf')
            if idx >= n or picked == k: return 0
            if cache[idx][picked] != -1: return cache[idx][picked]

            tmp, maxi = 0, float('-inf')
            for pile_idx in range(min(len(piles[idx]), k)):
                tmp += piles[idx][pile_idx]
                maxi = max(maxi,  solve(idx+1, picked+pile_idx+1) + tmp)

            cache[idx][picked] = max(maxi, solve(idx+1, picked))
            return cache[idx][picked]
        
        
        return solve(0, 0)
            