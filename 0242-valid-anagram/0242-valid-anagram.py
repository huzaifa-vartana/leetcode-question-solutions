class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        s_counter = Counter(s)
        t_counter = Counter(t)

        for i in range(len(s)):
            s_char, t_char = s[i], t[i]
            if s_counter[s_char] != t_counter[s_char]: return False


        return True