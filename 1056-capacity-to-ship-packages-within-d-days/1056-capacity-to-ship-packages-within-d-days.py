class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        n = len(weights)
        left, right = max(weights), sum(weights)
        ans = right

        while left <= right:
            capacity = (left+right) // 2
            possible = self.is_pos(weights, days, capacity)

            if possible:
                ans = capacity
                right = capacity - 1
            else:
                left = capacity + 1

        return ans
    
    def is_pos(self, weights, days, capacity):
        n = len(weights)
        count = 1
        total = 0
        for i in range(n):
            total += weights[i]
            if weights[i] > capacity:
                return False
            if total > capacity:
                count += 1
                total = weights[i]
        return count <= days