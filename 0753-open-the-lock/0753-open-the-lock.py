class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        start = "0000"
        q = deque([start])
        if start == target: return 0
        
        if start in deadends or target in deadends: return -1
        time = 0
        def gen_up(old, idx):
            return old[:idx] + str((int(old[idx]) + 1) % 10) + old[idx+1:]
            
        def gen_down(old, idx):
            return old[:idx] + str((int(old[idx]) - 1) % 10) + old[idx+1:]


        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                for wheel in range(4):
                    up = gen_up(curr, wheel)
                    down = gen_down(curr, wheel)

                    if up == target or down == target: return time + 1
                    if up not in deadends:
                        q.append(up)
                        deadends.add(up)
                    if down not in deadends:
                        q.append(down)
                        deadends.add(down)

            time += 1

        return -1
        