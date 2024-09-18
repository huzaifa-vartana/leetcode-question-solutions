class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * (len(nums) + 1)
        prefix[0] = 1
        for idx in range(1, len(nums) + 1):
            prefix[idx] = prefix[idx - 1] * nums[idx - 1]


        suffix = [0] * (len(nums) + 1)
        suffix[-1] = 1
        for idx in range(len(nums) - 1, -1, -1):
            suffix[idx] = suffix[idx + 1] * nums[idx]

        output = [0] * len(nums)
        for idx in range(len(nums)):
            output[idx] = prefix[idx] * suffix[idx + 1]

        return output