class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        N, M = len(haystack), len(needle)
        idx1, idx2 = 0, 0

        while idx1 < N:
            curr = idx1
            while curr < N and idx2 < M and haystack[curr] == needle[idx2]:
                idx2 += 1
                curr += 1

            if idx2 >= M: return idx1
            idx1 += 1
            idx2 = 0


        return -1

