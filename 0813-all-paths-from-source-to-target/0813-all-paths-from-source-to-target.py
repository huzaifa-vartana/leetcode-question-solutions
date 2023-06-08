class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        res = []
        n = len(graph)
        def dfs(node, curr):
            curr.append(node)
            if node == n - 1:
                res.append(curr.copy())
                return

            for nei in graph[node]:
                dfs(nei, curr)
                if curr: curr.pop()

        
        dfs(0, [])
        return res