class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adj = defaultdict(list)
        in_degree = [0] * numCourses
        for a, b in prerequisites:
            in_degree[a] += 1
            adj[b].append(a)

        res, q = [], []
        for c in range(numCourses):
            if in_degree[c] == 0: q.append(c)

        while q:
            node = q.pop(0)
            res.append(node)
            for neighbor in adj[node]:
                in_degree[neighbor] -=1
                if in_degree[neighbor] == 0: q.append(neighbor)


        return res if len(res) == numCourses else []