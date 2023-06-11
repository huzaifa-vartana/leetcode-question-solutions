class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        nums = list(map(lambda x: str(x), nums))

        def custom_sort(a, b):
            if a + b > b + a:
                return 1
            elif a + b < b + a:
                return -1
            else:
                return 0

        nums.sort(key=cmp_to_key(custom_sort), reverse=True)

        return str(int(''.join(nums)))