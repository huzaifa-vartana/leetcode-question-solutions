class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        
        def is_pal(left, right):
            
            
            while left <= right:
                if s[left] != s[right]: return False
                left += 1
                right -= 1
            
            return True
        
        n, res = len(s), []
        
        def solve(idx, pal_strs):
            if idx >= n:
                res.append(pal_strs)
                
            for k in range(idx, n):
                tmp = s[idx:k+1]
                if is_pal(idx, k): solve(k+1, pal_strs + [tmp])
            
        solve(0, [])
        return res