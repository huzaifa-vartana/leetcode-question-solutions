class MedianFinder:

    def __init__(self):
        # two heaps
        # min-heap and max-heap
        self.small = [] # max-heap
        self.large = [] # min-heap

    def addNum(self, num: int) -> None:

        # add first in the  small heap
        heappush(self.small, -num)

        if self.small and self.large and -self.small[0] > self.large[0]:
            heappush(self.large, -heappop(self.small))

        # both heap length should be at most 1
        if len(self.small) > len(self.large) + 1:
            heappush(self.large, -heappop(self.small))
        # both heap length should be at most 1
        if len(self.large) > len(self.small) + 1:
            heappush(self.small, -heappop(self.large))


        

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        
        if len(self.large) > len(self.small):
            return self.large[0]

        return (-self.small[0] + self.large[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()