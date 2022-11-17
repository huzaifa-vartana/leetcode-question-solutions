class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:


        nums1 = [-1] + nums1
        nums2 = [-1] + nums2
        n = len(nums1)
        
        cache = [[-1 for _ in range(3)] for _ in range(n+1)]
        def solve(i, swapped):
            if i >= n: return 0
            if cache[i][swapped] != -1: return cache[i][swapped]

            prev_number1 = nums1[i-1]
            prev_number2 = nums2[i-1]

            if swapped: prev_number1, prev_number2 = prev_number2, prev_number1

            mini = float('inf')
            if nums1[i] > prev_number1 and nums2[i] > prev_number2: mini = min(mini, solve(i+1, False))


            if nums1[i] > prev_number2 and nums2[i] > prev_number1: mini = min(mini, 1 + solve(i+1, True))

            cache[i][swapped] = mini
            return mini
        
        return solve(1, False)