class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char != ']':
                stack.append(char)
            else:
                s, num = "", ""
                while stack and stack[-1] != '[':
                    s = stack.pop()  + s
                if stack:
                    stack.pop()
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                stack.append(s * int(num) )

        return "".join(stack)

