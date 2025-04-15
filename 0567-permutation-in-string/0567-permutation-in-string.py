from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        M, N = len(s1), len(s2)
        if M > N:
            return False
        count = Counter(s1)
        
        l = 0
        for r in range(N):
            count[s2[r]] -= 1
            if count[s2[r]] == 0:
                del count[s2[r]]
                
            if r - l + 1 > M:
                count[s2[l]] += 1
                l += 1
                if count[s2[l - 1]] == 0:
                    del count[s2[l - 1]]
            if not count:
                return True
        if not count:
            return True
                

        return False