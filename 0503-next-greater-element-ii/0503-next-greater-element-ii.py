class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        N = len(nums)
        res = [-1] * N
        stack = []
        
        # Iterate through the array twice to handle the circular nature
        for idx in range(2*N):
            num = nums[idx % N]
            while stack and num > nums[stack[-1] % N]:
                curr_idx = stack.pop()

                res[curr_idx] = num

            if idx < N: stack.append(idx)
        
        return res