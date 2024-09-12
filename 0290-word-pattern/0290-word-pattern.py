class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        p_to_s = {}
        s_to_p = {}

        s_split = s.split(" ")

        if len(s_split) != len(pattern): return False

        for char, word in zip(pattern, s_split):

            if char in p_to_s and p_to_s[char] != word:
                return False
            if word in s_to_p and s_to_p[word] != char:
                return False

            p_to_s[char] = word
            s_to_p[word] = char

        return True

        
        