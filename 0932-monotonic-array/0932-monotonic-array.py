class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:

        increasing, decreasing = True, True
        for idx in range(1, len(nums)):
            first_num = nums[idx-1]
            second_num = nums[idx]

            if first_num < second_num:
                increasing = False

            if first_num > second_num:
                decreasing = False
                

        return decreasing or increasing



        