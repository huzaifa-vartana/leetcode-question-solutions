from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:

        N = len(code)
        result = [0] * N
        
        if k == 0:
            return result

        # sliding window
        window_start, windwow_end = 0, 0
        if k > 0:
            window_start = 1
            window_end = k
        else:
            window_start = N + k
            window_end = N - 1
            
        
        # sum the first window
        window_sum = 0
        for i in range(window_start, window_end + 1):
            window_sum += code[i % N]
            
        result[0] = window_sum

        # slide the window
        for i in range(1, N):
            window_start = (window_start + 1) % N
            window_sum -= code[window_start - 1]
            window_end = (window_end + 1) % N
            window_sum += code[window_end]
            result[i] = window_sum
        

        return result