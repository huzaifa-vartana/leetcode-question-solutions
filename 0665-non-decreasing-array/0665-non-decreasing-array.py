class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        N = len(nums)
        mods = 0
        for idx in range(1, N):
            if nums[idx-1] > nums[idx]:
                if idx-2 in range(N) and nums[idx-2] > nums[idx]:
                    nums[idx] = nums[idx-1]
                else:
                    nums[idx-1] = nums[idx]
                mods += 1

        return mods <= 1
