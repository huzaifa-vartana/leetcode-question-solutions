from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:

        dests = {}
        for start, end in paths:
            dests[start] = end

        for start, end in paths:
            if end not in dests:
                return end
