class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        suffix = 1


        output = [1] * len(nums)
        for idx in range(len(nums)):
            output[idx] *= prefix
            prefix *= nums[idx]


        print(output)
        for idx in range(len(nums) - 1, -1, -1):
            output[idx] *= suffix
            suffix *= nums[idx]
        print(output)
        return output