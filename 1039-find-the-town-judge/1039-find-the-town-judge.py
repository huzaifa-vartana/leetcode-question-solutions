class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        in_degree = defaultdict(int)
        out_degree = defaultdict(int)

        for p1, p2 in trust:

            in_degree[p2] += 1
            out_degree[p1] += 1

        for p in range(1, n+1):
            if out_degree[p] == 0 and in_degree[p] == n - 1: return p

        return -1

