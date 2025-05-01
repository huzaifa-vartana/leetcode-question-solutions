class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count = 0
        if k <= 0: return count
        N = len(nums)
        left, prod = 0, 1
        
        for right in range(N):
            prod *= nums[right]
            while left <= right and prod >= k:
                prod //= nums[left]
                left += 1

            count += right - left + 1

        return count
        