class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}
        

        left = 0
        for right in range(len(nums)):
            
            if right - left > k:
                if nums[left] in seen: del seen[nums[left]]
                left += 1

            if nums[right] in seen:
                return True

            
            seen[nums[right]] = right

        return False

        