class Solution:
    def partition(self, s: str) -> List[List[str]]:
        output = []

        def palindrome(l, r):
            while l < r:
                if s[l] != s[r]: return False
                l += 1
                r -= 1
            return True

        def paritition_helper(idx, res):
            if idx >= len(s):
                output.append(res.copy())
                return

            for r in range(idx, len(s)):
                if palindrome(idx, r):
                    res.append(s[idx:r+1])
                    paritition_helper(r+1, res)
                    res.pop()



        paritition_helper(0, [])
        return output
        