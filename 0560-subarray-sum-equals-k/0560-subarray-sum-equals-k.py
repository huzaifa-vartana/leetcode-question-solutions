class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        summ = 0
        count = 0
        seen = defaultdict(int)
        seen[0] = 1
        for num in nums:
            summ += num

            count += seen[summ-k]
            seen[summ] += 1
        return count
        