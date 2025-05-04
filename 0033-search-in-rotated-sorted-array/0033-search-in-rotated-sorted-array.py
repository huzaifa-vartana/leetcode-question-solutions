class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low, high = 0, n - 1

        while low <= high:
            mid = (low+high) // 2
            if nums[mid] == target: return mid

            l, m, h = nums[low], nums[mid], nums[high]

            if l <= m:
                if l <= target <= m:
                    high = mid - 1 
                else:
                    low = mid + 1
            else:
                if m <= target <= h:
                    low = mid + 1
                else:
                    high = mid - 1 

        return -1