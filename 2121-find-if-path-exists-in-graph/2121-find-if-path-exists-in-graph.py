class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        adj = collections.defaultdict(list)
        for e1, e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)


        seen = set()
        def solve(starting_node):
            if starting_node == destination: return True
            seen.add(starting_node)
            for nei in adj[starting_node]:
                if nei == destination: return True
                if nei not in seen and solve(nei): return True

            return False

            
        return solve(source)
        