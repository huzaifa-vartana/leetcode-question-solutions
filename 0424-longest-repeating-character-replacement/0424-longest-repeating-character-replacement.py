class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = defaultdict(int)
        N, l, ans = len(s), 0, 0
        for r in range(N):
            r_char = s[r]

            seen[r_char] += 1

            if r - l + 1 - max(seen.values()) > k:
                seen[s[l]] -= 1
                l += 1
            
            ans = max(ans, r - l + 1)
            
        return ans