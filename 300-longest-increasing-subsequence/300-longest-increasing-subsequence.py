class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # 1. simple array recursion, pick and not pick, n^2 and n^2
        # 2. tabulation dp, n^2 and n
        # 3. sorting the array and using the binary search
        n = len(nums)
        cache = [1] * (n+1)
        maxi = 1
        for idx in range(1, n):
            for prev in range(idx):
                if nums[idx] > nums[prev]:
                    cache[idx] = max(
                        cache[idx],
                        1 + cache[prev]
                    )
                
            maxi = max(
                maxi,
                cache[idx]
            )
                
                
                
                
                
                
        return maxi