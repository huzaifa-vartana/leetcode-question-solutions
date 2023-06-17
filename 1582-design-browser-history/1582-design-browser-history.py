class BrowserHistory:

    def __init__(self, homepage: str):
        # self.forward = [homepage]
        # self.backward = [homepage]
        self.history = [homepage]
        self.pos = 0 

    def visit(self, url: str) -> None:
        while len(self.history) - 1 > self.pos:
            self.history.pop()
        self.history.append(url)
        self.pos +=1 


    def back(self, steps: int) -> str:
        while steps > 0 and self.pos > 0:
            steps -= 1
            self.pos -= 1

        return self.history[self.pos]

    def forward(self, steps: int) -> str:
        while self.pos < len(self.history) - 1 and steps > 0:
            steps -= 1
            self.pos += 1

        return self.history[self.pos]

        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)