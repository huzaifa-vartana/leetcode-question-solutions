class Solution:
    def maxScore(self, s: str) -> int:

        max_score = 0

        n = len(s)
        ones = [0] * (n+1)
        zeros = [0] * (n+1)
        for idx in range(n):
            digit = s[idx]

            if digit == '1':
                ones[idx] = ones[idx-1] + 1
            else:
                ones[idx] = ones[idx-1]

            if digit == '0':
                zeros[idx] = zeros[idx-1] + 1
            else:
                zeros[idx] = zeros[idx-1]

        for idx in range(1, n):
            score = zeros[idx-1] + ones[n-1] - ones[idx-1]
            max_score = max(max_score, score)

        return max_score