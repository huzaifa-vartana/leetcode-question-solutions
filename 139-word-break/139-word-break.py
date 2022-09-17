class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        wordDict = set(wordDict)
        n = len(s)
        cache = [False] * (n+1)
        cache[n] = True
        for idx in range(n-1, -1, -1):
            poss = False
            for i in range(idx, n):
                tmp = s[idx:i+1]
                if tmp in wordDict and cache[i+1]: poss = True
            
            cache[idx] = poss
        
        
        
        return cache[0]