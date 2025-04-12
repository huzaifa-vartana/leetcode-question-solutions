class Solution:
    def numOfSubarrays(self, nums: List[int], k: int, threshold: int) -> int:
        N = len(nums)
        l, ans, summ, = 0, 0, 0

        for r in range(N):
            summ += nums[r]

            if r - l + 1 > k:
                summ -= nums[l]
                l += 1

            if r - l + 1 == k and summ / k >= threshold: 
                ans += 1

        return ans