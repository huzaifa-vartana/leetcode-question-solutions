class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.nums = [0] * (n+1)
        for idx in range(1, n+1):
            self.nums[idx] = nums[idx-1] + self.nums[idx-1]


    def sumRange(self, left: int, right: int) -> int:

        return self.nums[right+1] - self.nums[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)