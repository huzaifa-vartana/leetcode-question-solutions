class Solution:
    def isPowerOfThree(self, n: int) -> bool:

        if n == 0: return False


        def solve(num):
            if num == 1:
                return True
            elif num < 1:
                return False
            else:
                return solve(num/3)

            return False


        return solve(n)