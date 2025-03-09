class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        N = len(nums)
        prefix = [0] * N
        if nums:
            prefix[0] = nums[0]

        for idx in range(1, N):
            prefix[idx] = prefix[idx-1] + nums[idx]

        print(prefix)
        for idx in range(N):
            left_sum = 0 if idx == 0 else prefix[idx-1]
            right_sum = 0 if idx == N - 1 else prefix[-1] - prefix[idx]

            if left_sum == right_sum: return idx

        return -1