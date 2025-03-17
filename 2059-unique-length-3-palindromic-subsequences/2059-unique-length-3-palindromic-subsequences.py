class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0
        for c in set(s):
            left_index, right_index = self.find_first_and_last_occurrences(s, c)

            if left_index < right_index:
                res += len(set(s[left_index+1: right_index]))

        return res
    

    def find_first_and_last_occurrences(self, s, c):
        left_index, right_index = -1, -1
        for idx in range(len(s)):
            if s[idx] == c:
                left_index = min(left_index, idx) if left_index != -1 else idx
                right_index = max(right_index, idx)

        return [left_index, right_index]
            
