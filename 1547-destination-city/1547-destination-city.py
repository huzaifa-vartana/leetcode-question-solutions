class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        paths_dict = {}
        for p1, p2 in paths:
            paths_dict[p1] = p2

        def dfs(node):
            if node not in paths_dict: return node
            return dfs(paths_dict[node])

        return dfs(paths[0][0])
        
        

