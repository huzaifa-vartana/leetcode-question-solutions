class Solution:
    def isPowerOfThree(self, n: int) -> bool:

        if n == 0: return False


        def solve(num):
            if num == 1: return True
            if num < 1: return False

            if solve(num/3): return True 

            return False




        return solve(n)