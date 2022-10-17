class Solution:
    def checkValidString(self, s: str) -> bool:
        
        n = len(s)
        cache = [[False for _ in range(n+1)] for _ in range(n+1)]
        cache[n][0] = True
        
        for idx in range(n-1, -1, -1):
            for open_paran in range(n-1, -1, -1):
                
                if s[idx] == '(':
                    cache[idx][open_paran] = cache[idx+1][open_paran+1] 
                elif s[idx] == ')':
                    cache[idx][open_paran] = cache[idx+1][open_paran-1]
                else:
                    cache[idx][open_paran] = cache[idx+1][open_paran+1] or cache[idx+1][open_paran-1] or cache[idx+1][open_paran] 


        
        return cache[0][0]