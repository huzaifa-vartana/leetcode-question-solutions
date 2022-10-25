class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        
        n = len(coins)
                        
        cache = [[0 for _ in range(amount + 1)] for _ in range(n + 1)]
        cache[n][amount] = 1
        
        
        for idx in range(n-1, -1, -1):
            for a in range(amount, -1, -1):
                count = 0
                tmp = a + coins[idx]
                if tmp in range(amount+1): count = cache[idx][tmp]

                cache[idx][a] = cache[idx+1][a] + count

        
        
        return cache[0][0]
        