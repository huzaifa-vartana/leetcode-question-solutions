from collections import deque
from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        q = deque(tickets)
        tickets_need_to_buy = tickets[k]
        time_taken = 0
        idx = k

        while tickets_need_to_buy > 0:
            curr = q.popleft()
            if curr > 0:
                time_taken += 1
                if idx == 0:
                    tickets_need_to_buy -= 1
                    idx = len(q)
                    idx += 1

            idx -= 1
            q.append(curr - 1)

        return time_taken
