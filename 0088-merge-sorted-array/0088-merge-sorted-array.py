class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = j = 0
        count = 0  # how many from nums2 have been inserted
        
        while i < m + count and j < n:
            if nums1[i] <= nums2[j]:
                i += 1
            else:
                # Shift nums1 right from i to m+count-1
                for k in range(m + count, i, -1):
                    nums1[k] = nums1[k - 1]
                nums1[i] = nums2[j]
                i += 1
                j += 1
                count += 1

        # If any nums2 elements are left, append them
        while j < n:
            nums1[m + count] = nums2[j]
            j += 1
            count += 1
