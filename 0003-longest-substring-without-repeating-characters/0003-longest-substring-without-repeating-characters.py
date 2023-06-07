class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        start, end = 0, 0

        longest_string_len = 0
        seen = set()


        while end < len(s):
            if s[end] in seen:
                while start <= end and s[end] in seen:
                    seen.remove(s[start])
                    start += 1
   
            seen.add(s[end])
            end += 1

            longest_string_len = max(longest_string_len, end - start)


        return longest_string_len











        