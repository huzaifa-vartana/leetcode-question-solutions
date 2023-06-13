class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        res = []
        def solve(idx, curr):
            if len(curr) == 4:
                if idx >= len(s):
                    res.append(".".join(curr))
                return

            for num_idx in range(idx, len(s)):
                num = s[idx:num_idx+1]
                if (len(num) > 1 and num[0]) != '0' and int(num) in range(256):
                    solve(num_idx+1, curr + [num])

        solve(0, [])
        return res