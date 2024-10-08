class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(l, r):
            while l < r:
                if s[l] != s[r]: return False
                l +=1 
                r -=1
            return True

        N = len(s)
        if is_palindrome(0, N-1): return True 
        start, end = 0, N - 1
        while start < end:
            if s[start] != s[end]: return is_palindrome(start, end-1) or is_palindrome(start+1, end)
            start += 1
            end -= 1
        return False


    
        