class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        
        n = len(nums)
        t = target
        tot = sum(nums)
        d = (tot-t) // 2
        if (tot-t) < 0 or (tot-t) % 2 != 0: 
            return 0
        
        cache = [[0 for _ in range(d+1)] for _ in range(n+1)]
        cache[n][d] = 1
        for idx in range(n-1, -1, -1):
            for t in range(d, -1, -1):
                
                add =  0
                tmp = t + nums[idx]
                if tmp in range(d+1):
                    add = cache[idx+1][tmp]
                cache[idx][t] = cache[idx+1][t] + add

        
        

        return cache[0][0]
            
        
        
        