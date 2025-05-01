class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # dynamic sliding window, hashmap
        N = len(s)
        max_length, count = 0, defaultdict(int)
        left, right = 0, 0

        while right < N:

            count[s[right]] += 1
            while (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)
            right += 1

        return max_length
        