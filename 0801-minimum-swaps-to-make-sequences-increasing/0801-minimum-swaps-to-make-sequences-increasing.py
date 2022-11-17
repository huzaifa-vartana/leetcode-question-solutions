class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:


        nums1 = [-1] + nums1
        nums2 = [-1] + nums2
        n = len(nums1)
        
        cache = [[0 for _ in range(3)] for _ in range(n+1)]
        for i in range(n-1, 0, -1):
            for swapped in [True, False]:
            
                prev_number1 = nums1[i-1]
                prev_number2 = nums2[i-1]

                if swapped: prev_number1, prev_number2 = prev_number2, prev_number1

                mini = float('inf')
                if nums1[i] > prev_number1 and nums2[i] > prev_number2: mini = min(mini, cache[i+1][False])


                if nums1[i] > prev_number2 and nums2[i] > prev_number1: mini = min(mini, 1 + cache[i+1][True])

                cache[i][swapped] = mini

        
        return cache[1][False]