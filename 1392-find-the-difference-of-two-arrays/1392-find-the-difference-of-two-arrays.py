class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        res = [[], []]
        nums1 = set(nums1)
        nums2 = set(nums2)

        for num1 in nums1:
            if num1 not in nums2: res[0].append(num1)

        for num2 in nums2:
            if num2 not in nums1: res[1].append(num2)

        return res
        