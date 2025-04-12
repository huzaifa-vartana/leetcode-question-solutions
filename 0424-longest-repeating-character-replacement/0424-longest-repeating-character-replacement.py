class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans, l, r = 0, 0, 0
        N = len(s)
        count = defaultdict(int)
        max_f = 0
        while r < N:
            count[s[r]] += 1
            max_f = max(max_f, count[s[r]])
            r += 1
            while r - l - max_f > k:
                count[s[l]] -= 1
                max_f = max(max_f, count[s[l]])
                l += 1
            ans = max(ans, r-l)
        return ans