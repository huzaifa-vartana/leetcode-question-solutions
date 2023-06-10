class Solution:
    def validPalindrome(self, s: str) -> bool:        
        def isPalindrome(i,s):
            start, end = 0 , len(s) - 1
            while start < end:
                if start == i:
                    start+=1
                elif end == i:
                    end -= 1
                
                if s[start]!=s[end]:
                    return False
                start +=1 
                end -=1
            return True     
        
        
        for i,j in enumerate(s):
            # print(s[:i]+s[i+1:])
            if isPalindrome(i,s):
                return True
        return False
        
        # print(isPalindrome("aabaa"))
        
        

        