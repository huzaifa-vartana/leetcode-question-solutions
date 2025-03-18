class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        nums = list(map(lambda x: str(x), nums))

   

        nums.sort(key=cmp_to_key(lambda x, y: (y + x > x + y) - (y + x < x + y)))
        if nums[0] == '0':
            return '0'

        return str(int(''.join(nums)))




        



        