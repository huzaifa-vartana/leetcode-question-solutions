from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        N = len(nums)

        ans = []
        print(nums)
        idx = 0
        
        while idx < N:
            num = nums[idx]

            l, r = idx + 1, N - 1
            while l < r:
                summ = num + nums[l] + nums[r]

                if summ == 0:
                    ans.append([num, nums[l], nums[r]])
                    while l + 1 < N and nums[l] == nums[l+1]: l += 1
                    l += 1
                    while r - 1 > idx and nums[r] == nums[r-1]: r -= 1
                    r -= 1
                elif summ < 0:
                    l += 1
                else:
                    r -= 1            
            while idx + 1 < N and nums[idx] == nums[idx+1]: idx += 1
            idx += 1
            
        return ans