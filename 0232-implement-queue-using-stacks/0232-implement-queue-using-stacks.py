class MyQueue:

    def __init__(self):
        """
        s1 [1]
        s2 [1]

        """
        self.s1 = []
        self.s2 = []
        

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        if not self.s2: 
            while self.s1: 
                self.s2.append(self.s1.pop())

        return self.s2.pop()
    def peek(self) -> int:
        if not self.s2: 
            while self.s1: 
                self.s2.append(self.s1.pop())
        return self.s2[-1]
        

    def empty(self) -> bool:
        return not self.s1 and not self.s2