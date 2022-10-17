class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        
        MOD = 10 ** 9 + 7
        cache = [[0 for _ in range(target+1)] for _ in range(n+1)]
        cache[n][target] = 1
        
        for idx in range(n-1, -1, -1):
            for total_sum in range(target, -1, -1):
                count = 0
                for number in range(1, k+1):
                    tmp = total_sum + number
                    if tmp in range(target+1): count += cache[idx+1][tmp]

                cache[idx][total_sum] = count % MOD
        
        
        return cache[0][0]