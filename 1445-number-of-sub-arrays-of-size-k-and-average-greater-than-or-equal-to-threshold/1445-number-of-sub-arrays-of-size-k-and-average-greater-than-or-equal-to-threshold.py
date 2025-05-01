class Solution:
    def numOfSubarrays(self, nums: List[int], k: int, threshold: int) -> int:

        N = len(nums)
        left = 0
        count = 0
        subarray_sum = 0

        for right in range(N):
            subarray_sum += nums[right]

            if right - left + 1 > k:
                subarray_sum -= nums[left]
                left += 1


            if right - left + 1 == k and subarray_sum / k >= threshold:
                count += 1




        return count
        