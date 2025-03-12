class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        N = len(nums)
        
        for idx, num in enumerate(nums):
            special_num = N - idx
            if num >= special_num and (idx == 0 or nums[idx-1] < special_num):
                return special_num

        return -1