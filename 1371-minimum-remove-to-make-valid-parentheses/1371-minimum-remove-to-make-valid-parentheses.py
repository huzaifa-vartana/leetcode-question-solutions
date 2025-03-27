class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        s = list(s)

        for idx, char in enumerate(s):
            if char == "(":
                stack.append(idx)
            elif char == ")":
                if stack: stack.pop()
                else: s[idx] = ""
        
        for idx, remove in enumerate(stack):
            s[remove] = ""

        return "".join(s)





        