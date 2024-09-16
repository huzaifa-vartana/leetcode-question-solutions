class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time_taken = 0

        for i in range(len(tickets)):

            if i < k:
                time_taken += min(tickets[i], tickets[k])
            elif i == k:
                time_taken += tickets[k]
            else:
                time_taken += min(tickets[i], tickets[k] - 1)

        return time_taken