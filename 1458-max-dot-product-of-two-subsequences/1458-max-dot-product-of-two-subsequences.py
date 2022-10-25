class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)

        cache = [[[float('-inf') for _ in range(2)] for _ in range(n2+1)] for _ in range(n1+1)]
        for j in range(n2+1):
            cache[n1][j][True] = 0
        for i in range(n1+1):
            cache[i][n2][True] = 0
                
        for i in range(n1-1, -1, -1):
            for j in range(n2-1, -1, -1):
                for flag in [True, False]:
                    
                    a = cache[i+1][j][flag]
                    b = cache[i][j+1][flag] 
                    c = nums1[i] * nums2[j] + cache[i+1][j+1][True] 
                    d = cache[i+1][j+1][flag] 

                    cache[i][j][flag] = max(a, b, c, d)

        
        
        
        return cache[0][0][False]