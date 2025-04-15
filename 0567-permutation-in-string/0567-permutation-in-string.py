class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        M, N = len(s1), len(s2)
        if M > N:
            return False
        count1 = {}
        count2 = {}
        for r in range(M): count1[s1[r]] = count1.get(s1[r], 0) + 1
        
        l = 0
        for r in range(N):
            count2[s2[r]] = count2.get(s2[r], 0) + 1
            
            if r - l + 1 > M:
                count2[s2[l]] -= 1
                if count2[s2[l]] == 0:
                    del count2[s2[l]]
                l += 1
            if count1 == count2:
                return True

        
        return False