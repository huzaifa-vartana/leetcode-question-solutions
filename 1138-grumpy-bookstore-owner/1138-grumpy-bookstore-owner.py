class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], k: int) -> int:
        satisfied = 0

        n = len(customers)
        left = 0

        base, best_extra, curr_extra = 0, 0, 0
        for right in range(n):
            if grumpy[right] == 0:
                base += customers[right]
            else:
                curr_extra += customers[right]

            if right - left + 1 > k:
                if grumpy[left] == 1:
                    curr_extra -= customers[left]
                left += 1

            best_extra = max(curr_extra, best_extra)

        return base + best_extra


        