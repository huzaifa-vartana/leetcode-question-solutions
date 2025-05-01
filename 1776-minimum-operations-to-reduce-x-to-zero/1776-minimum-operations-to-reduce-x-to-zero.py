class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        N = len(nums)
        left, target = 0, sum(nums) - x
        max_subarray_count = -1  # Initialize as -1 in case target is never reached
        subarray_sum = 0

        for right in range(N):
            subarray_sum += nums[right]
            
            # shrink the window only if the sum exceeds the target
            while subarray_sum > target and left <= right:
                subarray_sum -= nums[left]
                left += 1
            
            # check for exact match
            if subarray_sum == target:
                max_subarray_count = max(max_subarray_count, right - left + 1)

        return N - max_subarray_count if max_subarray_count != -1 else -1
