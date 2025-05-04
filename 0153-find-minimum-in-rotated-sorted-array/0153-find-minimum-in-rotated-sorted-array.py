class Solution:
    def findMin(self, nums: List[int]) -> int:
        N = len(nums)
        low, high = 0, N - 1
        while low < high:
            mid = (low+high) // 2
            low_element, mid_element, high_element = nums[low], nums[mid], nums[high]

            if mid_element > high_element:
                low = mid + 1
            elif mid_element < low_element:
                high = mid
            else:
                high = mid - 1

        return nums[low]