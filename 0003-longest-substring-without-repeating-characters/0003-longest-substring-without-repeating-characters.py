class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        N = len(s)
        max_length, left = 0, 0
        seen = set()

        for right in range(N):
            
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length
        