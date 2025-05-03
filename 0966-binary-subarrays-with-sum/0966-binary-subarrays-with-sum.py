class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        seen = defaultdict(int)
        seen[0] = 1
        count, summ = 0, 0
        for num in nums:
            summ += num
            count += seen[summ-goal]
            seen[summ] += 1
        return count
        