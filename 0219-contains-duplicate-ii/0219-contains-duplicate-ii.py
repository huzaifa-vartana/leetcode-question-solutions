class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        N = len(nums)
        l, r = 0, 0
        seen = set()
        while r < N:
            if nums[r] in seen: return True
            
            seen.add(nums[r])
            r += 1

            if r - l > k:
                seen.remove(nums[l])
                l += 1
            
            

        return False