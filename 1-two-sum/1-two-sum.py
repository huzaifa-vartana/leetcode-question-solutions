class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        k=len(nums)

        for i in range(0,k):
            for j in range(i+1,k):
                if (target==nums[i]+nums[j]): return i,j
                

