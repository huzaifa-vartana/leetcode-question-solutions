class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        sum_map = {}

        for idx, num in enumerate(nums):
            rem_sum = target - num
            # sum_map[rem_sum] = idx
            if rem_sum in sum_map:
                return [sum_map[rem_sum], idx]
            else:
                sum_map[num] = idx


        return []