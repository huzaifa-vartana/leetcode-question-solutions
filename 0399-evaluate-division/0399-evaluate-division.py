from collections import defaultdict
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        adjacency_list = defaultdict(list)
        for idx in range(len(equations)):
            v1, v2 = equations[idx]
            val = values[idx]

            adjacency_list[v1].append((v2, val))
            adjacency_list[v2].append((v1, 1.0 / val))

        def dfs(start, end, visited):
            if start == end:
                return 1.0

            visited.add(start)
            for neighbor, value in adjacency_list[start]:
                if neighbor not in visited:
                    return_value = dfs(neighbor, end, visited)
                    if return_value != -1.0:
                        return value * return_value
                    else:
                        continue
            return -1.0

        output = []
        for v1, v2 in queries:
            if v1 not in adjacency_list or v2 not in adjacency_list:
                output.append(-1.0)
                continue
            output.append(dfs(v1, v2, set()))

        return output
