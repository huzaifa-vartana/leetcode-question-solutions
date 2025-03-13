class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ctr = {}

        res = -1
        for idx, char in enumerate(s):
            if char in ctr:
                first_index = ctr[char]
                ctr[char] = min(first_index, idx)
                res = max(res, idx - ctr[char] - 1)
            else:
                ctr[char] = idx

        
        
        return res