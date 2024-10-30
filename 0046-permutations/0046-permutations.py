class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        output = []

        def helper(idx):

            if idx >= len(nums):
                output.append(nums.copy())
                return
            
            for i in range(idx, len(nums)):
                nums[i], nums[idx] = nums[idx], nums[i]
                helper(idx+1)
                nums[i], nums[idx] = nums[idx], nums[i]

        helper(0)

        return output