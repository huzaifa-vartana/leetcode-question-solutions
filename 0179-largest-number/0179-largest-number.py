class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        def comparator(s1, s2):
            a=s1+s2
            b=s2+s1
            if a>b: return -1
            elif a<b: return 1
            else: return 0


        nums = list(map(str, nums))


        nums.sort(key=cmp_to_key(comparator))
        if nums[0] == '0': return '0'
        return "".join(nums)
        





        



        