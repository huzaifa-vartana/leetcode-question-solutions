class Solution:
    def bestClosingTime(self, customers: str) -> int:
        best_idx, best = 0, customers.count('Y')
        curr = best


        for idx in range(len(customers)):
            if customers[idx] == 'Y':
                curr -= 1
            else:
                curr += 1

            if curr < best:
                best_idx = idx + 1
                best = curr

        return best_idx