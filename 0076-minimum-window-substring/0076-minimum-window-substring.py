class Solution:
    def minWindow(self, s: str, t: str) -> str:
        N, M = len(s), len(t)

        t_freq_map = Counter(t)
        s_freq_map = {}

        left = 0
        min_string = ""
        min_string_len = float('inf')

        def is_valid():
            for k, v in t_freq_map.items():
                if s_freq_map.get(k, 0) < v:
                    return False
            return True

        # O (n) * 26
        for right in range(N):
            s_freq_map[s[right]] = s_freq_map.get(s[right], 0) + 1

            while is_valid():
                if right - left + 1 < min_string_len:
                    min_string_len = right - left + 1
                    min_string = s[left:right+1]

                s_freq_map[s[left]] -= 1
                if s_freq_map[s[left]] == 0: del s_freq_map[s[left]]
                left += 1


        return min_string


        