class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        paths_dict = {}
        for p1, p2 in paths:
            paths_dict[p1] = paths_dict.get(p1, 0) + 1
            paths_dict[p2] = paths_dict.get(p2, 0)

        for node, edges in paths_dict.items():
            if edges == 0: return node
        
        

