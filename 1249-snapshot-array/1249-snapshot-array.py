class SnapshotArray:

    def __init__(self, length: int):
        self.list = [[(0, 0)] for _ in range(length)]
        self.total_snaps = 0

    def set(self, index: int, val: int) -> None:
        self.list[index].append((self.total_snaps, val))

    def snap(self) -> int:
        self.total_snaps += 1
        return self.total_snaps - 1        

    def get(self, index: int, snap_id: int) -> int:
        history = self.list[index]
        ele = bisect.bisect_right(history, snap_id, key=lambda i: i[0])
        return history[ele-1][1]
        # left, right = 0, len(history) - 1
        # element = -1
        # while left < right:
        #     id, ele = history[(left+right)//2]

        #     if id == snap_id:

        #     elif id > snap_id:

        #     else:

        # return element
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)