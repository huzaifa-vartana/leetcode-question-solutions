class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        N = len(nums) - 1
        for i in range(N):
            if nums[i] != nums[i+1]:
                nums[k] = nums[i+1]
                k += 1
        return k
