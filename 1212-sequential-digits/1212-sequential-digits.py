class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        for starting_digit in range(1, 9):
            num = starting_digit
            for next_digit in range(starting_digit + 1, 10):
                num = num * 10 + next_digit
                if low <= num <= high:
                    ans.append(num)
                elif num > high:
                    break
            
        return sorted(ans)