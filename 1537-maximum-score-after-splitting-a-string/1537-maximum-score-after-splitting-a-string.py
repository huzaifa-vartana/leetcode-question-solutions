class Solution:
    def maxScore(self, s: str) -> int:

        max_score = 0

        n = len(s)
        ones = [0] * (n)
        zeros = [0] * (n)
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
        print(f"zeros: {zeros}")
        print(f"ones: {ones}")

        for idx1 in range(n-1):
            max_score = max(max_score, zeros[idx1] + ones[-1] - ones[idx1])

        return max_score
