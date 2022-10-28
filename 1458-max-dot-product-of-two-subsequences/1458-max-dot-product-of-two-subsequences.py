class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        
        m, n = len(nums1), len(nums2)
        
        @lru_cache(None)
        def solve(i = 0, j = 0, chosen = False):
            
            if i >= m or j >= n:
                return float('-inf') if not chosen else 0
            
            a = solve(i+1, j, chosen)
            b = solve(i, j+1, chosen)
            # c = solve(i+1, j+1, chosen)
            d = nums1[i] * nums2[j] + solve(i+1, j+1, True)
            
            return max(a, b, float('-inf'), d)
        
        
        
        
        return solve()