class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        N, l, base_satisfied_customers, extra_satisfied, max_extra_satisfied = len(customers), 0, 0, 0, 0

        for r in range(N):
            # handle base_satisfied_customers
            if grumpy[r] == 0:
                base_satisfied_customers += customers[r]
            else:
                extra_satisfied += customers[r]

            # handle invalid window
            if r - l + 1 > minutes:
                if grumpy[l] == 1:
                    extra_satisfied -= customers[l]
                l += 1
            
            max_extra_satisfied = max(max_extra_satisfied, extra_satisfied)



        return base_satisfied_customers + max_extra_satisfied
        