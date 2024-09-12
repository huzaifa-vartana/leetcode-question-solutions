class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = defaultdict(int)
        pos = 0
        for idx in range(len(nums)):
            num = nums[idx]
            if count[num] > 0:
                pos += count[num]
            count[num] += 1

        return pos