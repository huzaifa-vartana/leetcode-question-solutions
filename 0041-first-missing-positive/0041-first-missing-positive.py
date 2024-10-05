class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = len(nums)

        for idx in range(N):
            if nums[idx] <= 0 or nums[idx] > N:
                nums[idx] = N + 1

        for idx in range(N):
            num = abs(nums[idx])
            if num > N:
                continue
            if nums[num - 1] > 0:
                nums[num - 1] *= -1

        for idx in range(N):
            if nums[idx] > 0:
                return idx + 1

        return N + 1
