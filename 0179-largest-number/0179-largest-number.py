class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        nums = list(map(lambda x: str(x), nums))

   

        nums.sort(key=lambda x: x*10, reverse=True)

        return str(int(''.join(nums)))