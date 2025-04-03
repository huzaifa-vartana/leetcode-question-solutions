class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        num = "123456789"
        for i in range(len(num)):
            for j in range(i + 1, len(num) + 1):
                curr = int(num[i:j])
                if low <= curr <= high:
                    ans.append(curr)
                if curr > high:
                    break
            
        return sorted(ans)