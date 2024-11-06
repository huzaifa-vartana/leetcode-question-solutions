class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        N = len(s)

        output = []
        def helper(idx, res):

            if idx >= N:
                output.append(" ".join(res))
                return

            for j in range(idx, N):
                sub_str = s[idx:j+1]
                if sub_str in wordDict:
                    helper(j+1, res + [sub_str])

        helper(0, [])
        return output