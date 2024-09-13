class Solution:
    def largestGoodInteger(self, num: str) -> str:
        largest_good_int = float('-inf')

        idx = 0
        while idx < len(num):

            length = 1
            while idx + 1 < len(num) and num[idx] == num[idx+1]:
                idx += 1
                length += 1

            if length >= 3 and idx < len(num) and int(num[idx]) > largest_good_int:
                largest_good_int = int(num[idx])
            idx += 1

        if largest_good_int == float('-inf'): return ""
        return str(largest_good_int) * 3