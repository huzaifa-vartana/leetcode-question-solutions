class Solution:
    def minWindow(self, s: str, t: str) -> str:
        N, M = len(s), len(t)

        freq_map = {}
        for c in t: freq_map[c] = freq_map.get(c, 0) + 1

        left = 0
        min_string = ""
        min_string_len = float('inf')
        count = 0
        lenn = len(freq_map)

        for right in range(N):
            freq_map[s[right]] = freq_map.get(s[right], 0) - 1
            if freq_map[s[right]] == 0: count += 1

            while count == lenn:
                if right - left + 1 < min_string_len:
                    min_string_len = right - left + 1
                    min_string = s[left:right+1]

                freq_map[s[left]] += 1
                if freq_map[s[left]] > 0: count -= 1
                left += 1


        return min_string


        