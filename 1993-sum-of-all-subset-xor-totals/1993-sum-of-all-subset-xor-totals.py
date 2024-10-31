class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        def helper(idx, xor):
            if idx >= len(nums):
                return xor

            return helper(idx+1, xor ^ nums[idx]) + helper(idx+1, xor)
        
        return helper(0, 0)
        