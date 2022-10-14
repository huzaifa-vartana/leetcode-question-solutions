class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        cache = [float('inf')] * (amount+1)
        cache[0] = 0
        for change in range(1, amount+1):
            count = float('inf')
            for coin in coins:
                tmp = change-coin
                if tmp in range(amount+1): count = min(count, 1 + cache[tmp])
                    
            cache[change] = count
        
        
        
        tmp = cache[amount]
        return -1 if tmp == float('inf') else tmp