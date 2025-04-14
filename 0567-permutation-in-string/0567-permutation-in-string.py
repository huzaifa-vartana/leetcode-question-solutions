class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        M, N = len(s1), len(s2)
        if M > N:
            return False
        count1 = [0] * 26   
        count2 = [0] * 26
        for i in range(M):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1
        if count1 == count2:
            return True
        for i in range(M, N):
            count2[ord(s2[i]) - ord('a')] += 1
            count2[ord(s2[i - M]) - ord('a')] -= 1
            if count1 == count2:
                return True
        return False