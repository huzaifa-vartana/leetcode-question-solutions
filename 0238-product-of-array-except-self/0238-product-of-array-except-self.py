class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        N = len(nums)
        forward = [1] * N
        backward = [1] * N

        forward[0] = nums[0]
        backward[-1] = nums[-1]
        for idx in range(1, N):
            forward[idx] = forward[idx-1] * nums[idx]

        for idx in range(N-2, -1, -1):
            backward[idx] = backward[idx+1] * nums[idx]

        res = []
        for idx in range(N):
            if idx == 0:
                res.append(backward[idx+1])
            elif idx == N - 1:
                res.append(forward[idx-1])
            else:
                res.append(backward[idx+1] * forward[idx-1])

        return res

