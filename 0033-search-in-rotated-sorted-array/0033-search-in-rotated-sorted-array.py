class Solution:
    def search(self, nums: List[int], target: int) -> int:

        n = len(nums)
        low, high = 0, n - 1

        first_element, last_element = nums[0], nums[-1]

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target: return mid


            if nums[mid] > nums[high] and nums[mid] >= nums[low]:
                if target not in range(nums[low], nums[mid]+1): low = mid + 1
                else: high = mid - 1
            else:
                if target >= nums[mid] and target <= nums[high]: low = mid + 1
                else: high = mid - 1

        return -1
        