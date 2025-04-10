class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        [-2,1,-3,4,-1,2,1,-5,4]

        
        """
        g_max, l_max = nums[0], nums[0]

        for num in nums[1:]:
            l_max = max(l_max + num, num)
            g_max = max(g_max, l_max)


        return g_max
        