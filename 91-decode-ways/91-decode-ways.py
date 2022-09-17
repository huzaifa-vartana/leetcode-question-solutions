class Solution:
    def numDecodings(self, s: str) -> int:
        
        n = len(s)
        cache = [0] * (n+1)
        cache[n] = 1
        for idx in range(n-1, -1, -1):
            
            singleChar = int(s[idx])
            doubleChar = int(s[idx:idx+2])
            a, b = 0, 0
            if singleChar in range(1, 10): a = cache[idx+1]
            if doubleChar in range(10, 27): b = cache[idx+2]
            
            
            cache[idx] = a + b 
            
            
        return cache[0]
            