class Solution:
    def maxScore(self, s: str) -> int:

        max_score = 0
        zeros = 0
        n = len(s)
        for idx1 in range(n):
            if idx1 == n - 1: continue

            ones = 0
            if s[idx1] == "0":
                zeros += 1

            for idx2 in range(idx1+1, n):
                if s[idx2] == "1":
                    ones += 1
            max_score = max(max_score, zeros + ones)

        return max_score