class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:


        def prefix_exists(idx):
            for char_idx in range(1, len(strs)):
                if idx >= len(strs[char_idx]) or strs[char_idx][idx] != strs[0][idx]: return False

            return True

        longest = ""

        for idx in range(len(strs[0])):
            if prefix_exists(idx):
                longest += strs[0][idx]
            else:
                break


        return longest
