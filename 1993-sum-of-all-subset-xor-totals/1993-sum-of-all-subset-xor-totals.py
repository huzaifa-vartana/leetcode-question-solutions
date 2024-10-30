class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        output = []
        def helper(idx, res):
            if idx >= len(nums):
                output.append(res.copy())
                return 0

            res.append(nums[idx])
            helper(idx+1, res)
            res.pop()
            helper(idx+1, res)
        
        helper(0, [])
        
        total = 0
        for num  in output:
            xor = 0
            for n in num: 
                xor ^= n

            total += xor

        return total
        