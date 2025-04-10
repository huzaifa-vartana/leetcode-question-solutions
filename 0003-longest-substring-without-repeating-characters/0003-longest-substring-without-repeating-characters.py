class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l, r, ans = 0, 0, 0
        N = len(s)
        while r < N:
            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            seen.add(s[r])
            r += 1
            ans = max(ans, r - l)


        
        return ans