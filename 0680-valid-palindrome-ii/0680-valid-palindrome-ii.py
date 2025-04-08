class Solution:
    def validPalindrome(self, s: str) -> bool:
        N = len(s)
        def is_palindrome(left,right):
            start, end = left, right
            while start < end:
                if s[start]!=s[end]:
                    return False
                start +=1 
                end -=1
            return True     

        start, end = 0, N - 1
        if is_palindrome(start, end): return True
        while start < end:
            if s[start] != s[end]: 
                return is_palindrome(start+1, end) or is_palindrome(start, end-1)
            start += 1
            end -= 1

        return False