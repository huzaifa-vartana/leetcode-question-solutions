class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        output = []
        def helper(idx, res):

            output.append(res.copy())
            for i in range(idx, len(nums)):
                if i > idx and nums[i-1]==nums[i]:
                    continue
                res.append(nums[i])
                helper(i+1, res)
                res.pop()


        nums.sort()
        helper(0, [])
        return output
