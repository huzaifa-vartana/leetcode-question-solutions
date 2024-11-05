class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:

        def helper(idx, res):
            if idx >= len(nums):
                return 0 if not res else 1
            
            pos = True
            for num in res:
                if abs(num - nums[idx]) == k:
                    pos = False
                    break
            pick = 0
            if pos:
                res.append(nums[idx])
                pick += helper(idx+1, res)
                res.pop()

            not_pick = helper(idx+1, res)
            return pick + not_pick

        return helper(0, [])
        