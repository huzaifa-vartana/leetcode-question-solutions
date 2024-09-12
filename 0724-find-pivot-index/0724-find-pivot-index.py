class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum = [0] * (n+2)
        prefix_sum[0] = 0
        prefix_sum[1] = nums[0]
        prefix_sum[-1] = 0

        for idx in range(2, n+1):
            prefix_sum[idx] = prefix_sum[idx-1] + nums[idx-1]


        for idx in range(1, n+1):
            if prefix_sum[idx-1] == prefix_sum[-2] - prefix_sum[idx]:
                return idx-1
            
        return -1