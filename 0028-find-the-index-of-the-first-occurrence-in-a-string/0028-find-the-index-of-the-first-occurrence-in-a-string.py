class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        idx1, idx2 = 0, 0
        res = -1

        while idx1 < len(haystack):
            if haystack[idx1] == needle[idx2]:
                if res == -1: res = idx1
                idx1 += 1
                idx2 += 1
            else:
                res += 1
                while res < len(haystack) and haystack[res] != needle[0]:
                    res += 1
                idx1 = idx1 if res == -1 else res
                idx2 = 0
                res = -1
            if idx2 >= len(needle) and idx1 >= len(haystack):
                return res
            elif idx2 >= len(needle):
                return idx1 - idx2
            elif idx1 >= len(haystack):
                return -1


        return res
