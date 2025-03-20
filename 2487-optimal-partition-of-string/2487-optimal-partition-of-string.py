class Solution:
    def partitionString(self, s: str) -> int:
        N = len(s)
        left, right = 0, 0
        ans = 0

        while right <= N:
            while right < N and s[right] not in s[left:right]:
                right += 1
                
            ans += 1
            if right == N:
                break

            left = right
            right += 1
            
        
        return ans