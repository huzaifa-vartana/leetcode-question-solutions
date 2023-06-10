class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:

        adj = defaultdict(list)
        in_d = [0] * (n+1)


        for cr1, cr2 in relations:
            adj[cr1].append(cr2)
            in_d[cr2] += 1

        seen = set()
        q = deque()
        for cr in range(1, n+1):
            if in_d[cr] == 0:
                q.append(cr)
                seen.add(cr)


        dis = 0
        res = []
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                
                res.append(node)
                for nei in adj[node]:
                    in_d[nei] -= 1
                    if nei not in seen and in_d[nei] == 0:
                        q.append(nei)
                        seen.add(nei)
            dis += 1

        # print(res, dis)
        return dis if len(res) == n else -1


        