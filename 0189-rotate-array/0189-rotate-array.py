class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        nums = [1,2,3,4,5,6,7], k = 3
        7654321
        5671234
        nums = [-1,-100,3,99], k = 2
        99,3,-100,-1
        3,99,-1,-100
        """
        N = len(nums)
        k %= N
        self.reverse_list(nums, 0, N - 1)
        self.reverse_list(nums, k, N - 1)
        self.reverse_list(nums, 0, k - 1)


    def reverse_list(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end   -= 1
        
        return nums