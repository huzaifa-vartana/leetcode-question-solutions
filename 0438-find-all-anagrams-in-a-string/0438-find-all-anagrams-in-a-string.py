class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ctr = Counter(p)
        left, right, N = 0, 0, len(s)
        window_ctr, res = defaultdict(int), []

        while right < N:
            left_char, right_char = s[left], s[right]

            if right_char not in ctr:
                right += 1
                left = right
                window_ctr.clear()
            else:
                if window_ctr[right_char] < ctr[right_char]:
                    right += 1
                    window_ctr[right_char] += 1
                    if right - left == len(p):
                        res.append(left)
                        window_ctr[left_char] -= 1
                        left += 1
                else:
                    left += 1
                    window_ctr[left_char] -= 1


        return res
    