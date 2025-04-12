class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        N = len(customers)
        total = sum(customer for customer, is_grumpy in zip(customers, grumpy) if not is_grumpy)
        print(total)
        
        l, ans, local_all, local_real = 0, 0, 0, 0
        for r in range(N):
            local_all += customers[r]
            if grumpy[r] == 0:
                local_real += customers[r]
            
            if r - l + 1 > minutes:
                local_all -= customers[l]
                if grumpy[l] == 0:
                    local_real -= customers[l]
                l += 1
            if r - l + 1 == minutes:
                ans = max(ans, total + local_all - local_real)

        return ans


        

