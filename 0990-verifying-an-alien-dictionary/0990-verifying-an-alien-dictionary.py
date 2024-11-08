from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        lookup = {char: idx for idx, char in enumerate(order)}

        for idx in range(len(words)-1):
            curr, next = words[idx], words[idx+1]
            len1, len2 = len(curr), len(next)

            i, j = 0, 0
            all_same = True
            while i < len1 or j < len2:
                if i in range(len1) and j in range(len2) and lookup[curr[i]] < lookup[next[j]]:
                    break

                if i in range(len1) and j in range(len2) and lookup[curr[i]] != lookup[next[j]]:
                    all_same = False
                if i in range(len1) and j in range(len2) and lookup[curr[i]] > lookup[next[j]]:
                    return False

                if i in range(len1) and j not in range(len2) and all_same:
                    return False
                if i in range(len1) and j not in range(len2) and not all_same:
                    break

                i += 1
                j += 1

        return True

