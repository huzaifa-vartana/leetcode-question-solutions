class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0

        counter = Counter(nums)
        for key, freq in counter.items():
            if freq == 1:
                return -1

            if freq % 3 == 0:
                ans += freq // 3
            else:
                ans += freq // 3 + 1
            


        return ans