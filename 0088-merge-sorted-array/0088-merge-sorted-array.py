class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j, k = m - 1, n - 1, len(nums1) - 1

        # i -> end of actual items in nums1
        # j -> end of nums2
        # k -> end of nums1
        while i >= 0 and j >= 0:
            if nums2[j] >= nums1[i]:
                nums1[k] = nums2[j]
                j -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1

            k -= 1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1