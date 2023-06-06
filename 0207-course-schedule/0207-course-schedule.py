class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # prerequisites[i] = [a, b]
        # b depends on a
        

        adj = defaultdict(list)
        for course1, course2 in prerequisites:
            adj[course2].append(course1)

        # check cycle not present
        # cal toposort

        seen, curr_seen = set(), set()
        def dfs(node):
            seen.add(node)
            curr_seen.add(node)

            for nei in adj[node]:
                if nei not in seen and dfs(nei): return True
                elif nei in curr_seen: return True

            curr_seen.remove(node)
            return False

        for course in range(numCourses):
            if course not in seen and dfs(course): return False

        return True


