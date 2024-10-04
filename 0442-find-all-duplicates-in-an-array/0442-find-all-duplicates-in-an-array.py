class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        N = len(nums)
        res = []

        for idx in range(1, N+1):
            new_idx = abs(nums[idx - 1])
            new_idx = new_idx - 1

            if nums[new_idx] < 0:
                res.append(new_idx+1)
            else:
                nums[new_idx] = -nums[new_idx]

        return res