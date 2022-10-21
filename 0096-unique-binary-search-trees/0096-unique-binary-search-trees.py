class Solution:
    def numTrees(self, n: int) -> int:
        
        @lru_cache(None)
        def solve(n):
            if n <= 1:
                return 1

            count = 0
            for root in range(1, n+1):
                count += solve(root-1) * solve(n-root)

            return count
        
        return solve(n)