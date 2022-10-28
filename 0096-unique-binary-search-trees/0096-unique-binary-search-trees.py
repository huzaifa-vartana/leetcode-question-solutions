class Solution:
    def numTrees(self, n: int) -> int:
        
        
        cache = [0] * (n+1)
        cache[0] = cache[1] = 1
        
        for t in range(2, n+1):
            
            count = 0
            for root in range(1, t+1):
                count += cache[root-1] * cache[t-root]
                
            cache[t] = count
        
        
        
        return cache[n]