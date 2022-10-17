class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        
        MOD = 10 ** 9 + 7

        @lru_cache(None)
        def solve(idx, total_sum):
            if idx == n: return 1 if total_sum == target else 0
            if total_sum > target: return 0
            
            count = 0
            for number in range(1, k+1):
                count += solve(idx+1, total_sum + number)
                
            return count % MOD
        
        
        return solve(0, 0)