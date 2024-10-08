class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        N, M = len(word1), len(word2)
        i, j = 0, 0
        res = ""
        while i < N or j < M:
            if i < N:
                res += word1[i]
            if j < M:
                res += word2[j]

            i += 1
            j += 1

        return res
        