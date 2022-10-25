class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)

        @lru_cache(None)
        def solve(i, j, flag):
            if i == n1 or j == n2:
                return float('-inf') if not flag else 0

            a = solve(i+1, j, flag)
            b = solve(i, j+1, flag)
            c = nums1[i] * nums2[j] + solve(i+1, j+1, True)
            d = solve(i+1, j+1, flag)

            return max(a, b, c, d)
        
        
        
        return solve(0, 0, False)