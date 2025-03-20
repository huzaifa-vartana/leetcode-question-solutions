class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        N = len(s)
        left, right = 0, 0
        if N < k:
            return False
        if N == k:
            return len(set(s)) == 2 ** k

        distinct_substrings = set()
        while right <= N:

            while right - left  < k:
                right += 1

            if right - left == k:
                distinct_substrings.add(s[left:right])
            if len(distinct_substrings) == 2 ** k:
                return True
            
            left += 1
            right += 1
            
        return False