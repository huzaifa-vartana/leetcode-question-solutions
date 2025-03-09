class NumArray:

    def __init__(self, nums: List[int]):
        N = len(nums)
        self.prefix = [0] * (N+1)
        for idx in range(1, N+1):
            self.prefix[idx] = self.prefix[idx-1] + nums[idx-1]

        print(self.prefix)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right+1] - self.prefix[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)