class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:

        N = len(s)
        ans = 0
        for c in range(26):
            i, j = N, -1
            for k in range(N):
                if ord(s[k]) - ord('a') == c:
                    i = min(i, k)
                    j = max(j, k)
            ans += len(set(s[i + 1: j]))

        return ans

