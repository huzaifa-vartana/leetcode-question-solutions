class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_dict = {nums1[i]: i for i in range(len(nums1))}
        stack = []
        ans = [-1] * len(nums1)

        for idx in range(len(nums2)-1, -1, -1):
            num = nums2[idx]
            while stack and num > stack[-1][1]:
                stack.pop()

            if stack and num in nums1_dict:
                ans[nums1_dict[num]] = stack[-1][1]

            stack.append((idx, num))

        return ans