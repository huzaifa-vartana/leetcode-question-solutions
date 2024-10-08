class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def rev(i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -=1

        N = len(nums)
        k = k % N
        nums.reverse()
        rev(0,k-1)
        rev(k, N-1)
        
        


        