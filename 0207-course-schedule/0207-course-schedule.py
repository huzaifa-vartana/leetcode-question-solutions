class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj = defaultdict(list)
        for c1, c2 in prerequisites: adj[c1].append(c2)

        def toposort(node, seen, curr_path):
            seen.add(node)
            curr_path.add(node)

            for neighbor in adj[node]:
                if neighbor not in seen and toposort(neighbor, seen, curr_path): 
                    return True
                elif neighbor in curr_path: 
                    return True

            curr_path.remove(node)
            return False

        for course in range(numCourses):
            if toposort(course, set(), set()): return False

        return True


