class Solution:
    def maxArea(self, height: List[int]) -> int:
        N = len(height)
        start, end = 0, N - 1
        ans, best_left, best_right = 0, None, None
        while start < end:
            local_best = (end - start) * min(height[end], height[start])
            ans = max(ans, local_best)

            if height[start] > height[end]: end -= 1
            else: start += 1

        

        return ans
        