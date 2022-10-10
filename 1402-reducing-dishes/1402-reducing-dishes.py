class Solution:
    def maxSatisfaction(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        
        prev = [0 for _ in range(n+1)]
        for idx in range(n-1, -1, -1):
            curr = [0 for _ in range(n+1)]
            for cooked in range(n-1, -1, -1):
                curr[cooked] = max(
                    prev[cooked], 
                    nums[idx] * (cooked+1) + prev[cooked+1]
                )

            prev = curr

        return prev[0]