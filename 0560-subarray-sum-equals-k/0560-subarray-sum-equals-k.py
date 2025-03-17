class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        N = len(nums)
        count = 0

        sub_array_sum_count = { 0: 1 }
        sub_array_sum = 0

        for num in nums:
            sub_array_sum += num

            if (sub_array_sum - k) in sub_array_sum_count:
                count += sub_array_sum_count[(sub_array_sum - k)]

            sub_array_sum_count[sub_array_sum] = sub_array_sum_count.get(sub_array_sum, 0) + 1

        return count