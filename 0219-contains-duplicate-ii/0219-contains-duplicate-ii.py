class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        l = 0

        for r in range(len(nums)):

            r_num = nums[r]
            l_num = nums[l]
            

            if r - l > k:
                seen.remove(l_num)
                l += 1

            if r_num in seen:
                return True
            seen.add(r_num)
        
        return False
        