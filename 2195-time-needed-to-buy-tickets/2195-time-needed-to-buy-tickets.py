from collections import deque
from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        q = deque(tickets)

        time = 0
        while True:
            p = q.popleft()

            if k == 0 and p-1 == 0:
                return time + 1

            if p-1 > 0:
                q.append(p-1)

            k = len(q) - 1 if k == 0 else k - 1
            time += 1
