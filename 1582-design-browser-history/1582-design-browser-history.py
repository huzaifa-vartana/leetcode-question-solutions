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
        steps_can_go_back = min(self.pos, steps)
        for _ in range(self.pos, self.pos - steps_can_go_back, -1):
            self.pos -= 1

        return self.history[self.pos]

    def forward(self, steps: int) -> str:
        steps_can_go_forw = min(len(self.history) - self.pos - 1, steps)
        for _ in range(self.pos, self.pos + steps_can_go_forw):
            self.pos += 1

        return self.history[self.pos]

        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)