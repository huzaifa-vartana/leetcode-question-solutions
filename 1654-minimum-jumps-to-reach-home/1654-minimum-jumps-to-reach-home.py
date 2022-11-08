class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        
        q = [(0, False)]
        seen = set(forbidden)
        seen.add((0, False))
        mini = 0

        while q:
            for _ in range(len(q)):
                n, jump_b = q.pop(0)
                if n == x:
                    return mini

                if not jump_b and n-b >= 0 and (n-b) not in forbidden and (n-b, True) not in seen:
                    q.append((n-b, True))
                    seen.add((n-b, True))

                if n+a < 10000 and (n+a) not in forbidden and (n+a, False) not in seen:
                    q.append((n+a, False))
                    seen.add((n+a, False))

            mini += 1

        return -1