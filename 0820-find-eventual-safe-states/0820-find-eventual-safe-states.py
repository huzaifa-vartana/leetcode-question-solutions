class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        n = len(graph)

        seen = set()
        curr_seen = set()

        def detect_cycle(node):
            seen.add(node)
            curr_seen.add(node)
            for nei in graph[node]:
                if nei not in seen and detect_cycle(nei): return True
                elif nei in curr_seen: return True

            curr_seen.remove(node)
            return False

        res = []
        for node in range(n):
            if not detect_cycle(node):
                res.append(node)

        return res



                


