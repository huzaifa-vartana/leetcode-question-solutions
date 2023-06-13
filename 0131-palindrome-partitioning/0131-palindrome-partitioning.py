class Solution:
    def partition(self, s: str) -> List[List[str]]:



        def pal(l, r):
            while l <= r:
                if s[l] != s[r]: return False
                l += 1
                r -= 1
            return True


        res = []
        def solve(idx, curr):

            if idx >= len(s):
                res.append(curr)
                return

            for char_idx in range(idx, len(s)):
                substr = s[idx:char_idx+1]
                if pal(idx, char_idx):
                    solve(char_idx+1, curr + [substr])





            return -1

        solve(0, [])
        return res
