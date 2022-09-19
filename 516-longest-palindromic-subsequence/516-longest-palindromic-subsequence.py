class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        s, t = s, s[::-1]
        n = len(s)
        cache = [[-1 for _ in range(n+1)] for _ in range(n+1)]
        def solve(left, right):
            
            if left > right: return 0
            if left == right: return 1
            if cache[left][right] != -1: return cache[left][right]
            
            if s[left] == s[right]:
                return 2 + solve(left+1, right-1)
            
            cache[left][right] =  max(solve(left+1, right), solve(left, right-1))
            return cache[left][right] 
        
        
        return solve(0, n-1)