class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:


        def prefix_exists(idx):
            prefix = strs[0][:idx+1]
            print(prefix)
            for char_idx in range(1, len(strs)):
                if strs[char_idx][:idx+1] != prefix: return False

                
            return True
        longest = ""

        for idx in range(len(strs[0])):
            prefix = strs[0][:idx+1]
            if prefix_exists(idx):
                longest = max(longest, prefix, key=len)
            else:
                break


        return longest