class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:

        def helper(idx, res):
            if idx >= len(nums):
                return 0 if not res else 1
            
            pick = 0
            if not res[nums[idx] - k] and not res[nums[idx] + k]:
                res[nums[idx]] += 1
                pick += helper(idx+1, res)
                res[nums[idx]] -= 1

            not_pick = helper(idx+1, res)
            return pick + not_pick

        return helper(0, defaultdict(int)) - 1
        