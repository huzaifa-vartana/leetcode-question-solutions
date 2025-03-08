class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        el, cnt = None, 0


        for num in nums:
            if cnt == 0:
                el = num

            if el == num: cnt += 1
            else: cnt -= 1
            


        return el
        