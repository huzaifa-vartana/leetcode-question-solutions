class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        count = 0
        ele = -1

        for num in nums:
            if count == 0:
                ele = num
                count += 1
                continue

            if ele == num:
                count += 1
            else:
                count -=1

        return ele
            

            
        