class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        
        max_so_far = nums[0]
        max_sum_array_sum = nums[0]

        for num in nums[1:]:

            max_so_far = max(max_so_far + num, num)
            max_sum_array_sum = max(max_sum_array_sum, max_so_far)




        return max_sum_array_sum
