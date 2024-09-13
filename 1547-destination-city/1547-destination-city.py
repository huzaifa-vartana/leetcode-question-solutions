from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:

        dests = {}
        for start, end in paths:
            dests[start] = end

        def recursive_helper(start):
            if start not in dests:
                return start
            return recursive_helper(dests[start])

        return recursive_helper(paths[0][0])