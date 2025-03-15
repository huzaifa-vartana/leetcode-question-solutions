class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        [1,2,3,4]

        [1, 1, 2, 6]

        """
        N = len(nums)
        suf = 1
        pre = 1
        res = [1] * (N)

        for idx in range(N):
            res[idx] *= pre
            pre *= nums[idx]

        for idx in range(N-1, -1, -1):
            res[idx] *= suf
            suf *= nums[idx]


        return res