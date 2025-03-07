class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        len_ = len(s)
        idx = len_ - 1

        last_word = 0
        while idx >= 0:
            char = s[idx]

            if char == " ":
                if last_word > 0: break
                idx -=1
                continue

            last_word += 1
            idx -= 1




        return last_word