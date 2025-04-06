class MyQueue:

    def __init__(self):
        """
        push 1
        push 2
        peek 1
        pop 1
        empty false

        s1 [1, 2]
        s2 [0, ]

        """
        self.stack = []
        self.top = 0
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        

    def pop(self) -> int:
        ele = self.stack[self.top]
        self.top += 1
        return ele
        

    def peek(self) -> int:
        return self.stack[self.top]
        

    def empty(self) -> bool:
        return self.top >= len(self.stack)