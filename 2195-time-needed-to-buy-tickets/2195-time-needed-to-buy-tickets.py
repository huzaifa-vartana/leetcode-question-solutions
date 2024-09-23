class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:

        time = 0
        N = len(tickets)
        for idx in range(N):
            ticket = tickets[idx]

            if idx == k:
                time += ticket
            elif idx > k:
                time += min(ticket, tickets[k] - 1)
            elif idx < k:
                time += min(ticket, tickets[k])


        





        return time
        