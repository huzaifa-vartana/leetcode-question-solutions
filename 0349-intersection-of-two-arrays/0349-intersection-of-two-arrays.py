class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        uniq_nums1 = set(nums1)
        res = []
        for num in nums2:
            if num in uniq_nums1: 
                res.append(num)
                uniq_nums1.remove(num)



        return res
        