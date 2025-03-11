class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        for idx, ticket in enumerate(tickets):

            if idx == k:
                time += ticket
            elif idx > k:
                time += min(ticket, tickets[k] - 1)
            else:
                time += min(ticket, tickets[k])


        return time