class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(['a', 'e', 'i', 'o', 'u'])

        N = len(s)

        best = 0
        l = 0
        curr = 0

        for r in range(N):
            if s[r] in vowels:
                curr += 1

            if r - l + 1 > k:
                if s[l] in vowels: curr -= 1
                l += 1
            best = max(best, curr)

        return best
        