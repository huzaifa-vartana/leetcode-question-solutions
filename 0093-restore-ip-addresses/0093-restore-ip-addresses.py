class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        N = len(s)
        output = []
        def helper(idx, res):

            if idx >= N:
                if len(res) == 4:
                    output.append(".".join(res))
                return

            for i in range(idx, N):
                digits = s[idx:i+1]
                if len(digits) > 1 and digits[0] == "0":
                    continue

                if int(digits) in range(256):
                    helper(i+1, res + [digits])

            return

        helper(0, [])
        return output