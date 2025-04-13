class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l, N, max_length = 0, len(s), 0
        for r in range(N):
            while l < N and s[r] in seen:
                seen.remove(s[l])
                l += 1

            seen.add(s[r])
            max_length = max(max_length, r - l + 1)
            
        return max_length
        