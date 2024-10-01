from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        N, M = len(s), len(p)
        if N < M:
            return []
        p_count = Counter(p)
        s_count = Counter()
        res = []

        left = 0
        right = 0

        while right < N:
            if s[right] in p_count:
                if s_count[s[right]] < p_count[s[right]]:
                    s_count[s[right]] += 1
                    right += 1
                    if right - left == M:
                        res.append(left)
                        s_count[s[left]] -= 1
                        left += 1

                else:
                    s_count[s[left]] -= 1
                    left += 1
            else:
                s_count.clear()
                right += 1
                left = right

        return res

