class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater_element = {}
        for idx in range(len(nums2)):
            num = nums2[idx]

            next_greater_element[num] = -1
            for next_num in nums2[idx+1:]:
                if next_num > num:
                    next_greater_element[num] = next_num
                    break

        output = []
        for num in nums1:
            output.append(next_greater_element[num])

        return output