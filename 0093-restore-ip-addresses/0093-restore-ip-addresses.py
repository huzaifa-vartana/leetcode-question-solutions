class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        res = []
        def solve(idx, curr):
            if len(curr) == 4:
                if idx >= len(s):
                    res.append(".".join(curr))
                return
            if idx >= len(s):
                return

            # rules for IP-addr
            # rule 1. Each integer is between 0 and 255 (inclusive)
            # rule 2. Cannot have leading zeros.

            for num_idx in range(idx, len(s)):
                num = s[idx:num_idx+1]

                # print(num)
                if (len(num) > 1 and num[0]) != '0' and int(num) in range(256):
                    solve(num_idx+1, curr + [num])

        solve(0, [])
        return res