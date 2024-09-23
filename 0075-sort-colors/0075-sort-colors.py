class Solution:
    def sortColors(self, nums: List[int]) -> None:
        N = len(nums)
        start, mid, end = 0, 0, N - 1

        while mid <= end:
            if nums[mid] == 0:
                nums[start], nums[mid] = nums[mid], nums[start]
                start += 1
                mid += 1

            elif nums[mid] == 1:
                mid += 1
            elif nums[mid] == 2:
                nums[end], nums[mid] = nums[mid], nums[end]
                end -= 1


        