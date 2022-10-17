class Solution:
    def checkValidString(self, s: str) -> bool:
        
        n = len(s)
        cache = [[-1 for _ in range(n+1)] for _ in range(n+1)]
        
        def solve(idx, open_paran):
            
            if open_paran < 0: return False
            if idx >= n: return True if open_paran == 0 else False
            if cache[idx][open_paran] != -1: return cache[idx][open_paran]
            
            if s[idx] == '(':
                cache[idx][open_paran] = solve(idx+1, open_paran+1) 
            elif s[idx] == ')':
                cache[idx][open_paran] = solve(idx+1, open_paran-1)
            else:
                cache[idx][open_paran] = solve(idx+1, open_paran+1) or solve(idx+1, open_paran-1) or solve(idx+1, open_paran)
                
                
            return cache[idx][open_paran]
        
        return solve(0, 0)