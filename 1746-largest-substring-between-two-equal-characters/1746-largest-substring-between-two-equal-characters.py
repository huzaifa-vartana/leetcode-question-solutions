class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ctr = {}

        res = -1
        for idx, char in enumerate(s):
            if char in ctr:
                first_index, last_index = ctr[char]
                ctr[char] = [min(first_index, idx), max(last_index, idx)]
                res = max(res, ctr[char][1] - ctr[char][0] - 1)
            else:
                ctr[char] = [idx, idx]

        
        
        return res