class Solution:
    def combinationSum(self, nums: List[int], k: int) -> List[List[int]]:
        ans = []
        
        def recurse(idx, res, sum_):

            if idx >= len(nums):
                if sum_ == k:
                    ans.append(res)
                return
            if sum_ > k: return

            recurse(idx, res + [nums[idx]], sum_ + nums[idx])
            recurse(idx+1, res, sum_)

        recurse(0, [], 0)
        return ans