class Solution:
    def totalFruit(self, nums: List[int]) -> int:

        n = len(nums)

        total, left = 0, 0
        types = {}

        for right in range(n):

            types[nums[right]] = types.get(nums[right], 0) + 1

            while len(types) > 2:
                types[nums[left]] -= 1
                if types[nums[left]] == 0: del types[nums[left]]
                left += 1
            total = max(total, right - left + 1)


        return total
        