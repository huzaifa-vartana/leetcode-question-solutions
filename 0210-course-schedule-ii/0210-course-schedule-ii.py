class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adj = defaultdict(list)
        for a, b in prerequisites: adj[a].append(b)

        res = []
        visited = set()
        def toposort(node, curr_path_visited):
            visited.add(node)
            curr_path_visited.add(node)

            for neighbor in adj[node]:
                if neighbor not in visited and toposort(neighbor, curr_path_visited): return True
                elif neighbor in curr_path_visited: return True

            res.append(node)
            curr_path_visited.remove(node)
            return False

        for v in range(numCourses):
            if v not in visited and toposort(v, set()): return []

        return res