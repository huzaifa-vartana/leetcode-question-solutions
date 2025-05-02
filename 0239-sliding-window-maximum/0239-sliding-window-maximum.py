from collections import Counter
from typing import List
from collections import deque, UserList


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        N = len(nums)
        deq = deque()
        for i in range(N):
            # Remove elements not in the window
            if deq and deq[0] == i - k:
                deq.popleft()
            # Remove smaller elements in k range as they are useless
            while deq and nums[deq[-1]] < nums[i]:
                deq.pop()
            deq.append(i)
            # Append the maximum element of the window
            if i >= k - 1:
                result.append(nums[deq[0]])
        # Return the result
        # The result is a list of the maximum elements in each sliding window
        # of size k
        # The deque stores the indices of the elements in the current window

        return result
