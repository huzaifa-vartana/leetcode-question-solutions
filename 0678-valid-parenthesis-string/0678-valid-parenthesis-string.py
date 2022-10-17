class Solution:
    def checkValidString(self, s: str) -> bool:
        
        n = len(s)
        prev = [False for _ in range(n+1)]
        prev[0] = True
        
        for idx in range(n-1, -1, -1):
            curr = [False for _ in range(n+1)]
            for open_paran in range(n-1, -1, -1):
                if s[idx] == '(':
                    curr[open_paran] = prev[open_paran+1] 
                elif s[idx] == ')':
                    curr[open_paran] = prev[open_paran-1]
                else:
                    curr[open_paran] = prev[open_paran+1] or prev[open_paran-1] or prev[open_paran] 

            prev = curr
        
        return prev[0]