class Solution:
    def maxScore(self, s: str) -> int:
        N = len(s)
        zeros = [0] * (N)
        ones = [0] * (N)

        if s[0] == "0": zeros[0] = 1
        if s[0] == "1": ones[0] = 1

        for idx in range(1, N):
            digit = s[idx]
            if digit == "0": 
                zeros[idx] = zeros[idx-1] + 1
            else:
                zeros[idx] = zeros[idx-1]
            
            if digit == "1": 
                ones[idx] = ones[idx-1] + 1
            else:
                ones[idx] = ones[idx-1]

        score = 0

        for idx in range(N-1):
            # print(s[:idx+1], s[idx+1:N], "zeros: ", zeros[idx], ones[-1] - ones[idx])
            score = max(
                zeros[idx] + ones[-1] - ones[idx],
                score
            )

        return score

        