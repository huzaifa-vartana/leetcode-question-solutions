class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], part: int) -> int:
        
        n = len(arr)
        cache = [0 for _ in range(n+1)]
        for idx in range(n-1, -1, -1):
        
            max_sum = 0
            itr = min(idx + part, n)
            for k in range(idx, itr):

                subarray_sum = max(arr[idx:k+1]) * (k - idx + 1)
                max_sum = max(max_sum, subarray_sum + cache[k+1])

            cache[idx] = max_sum
        
        return cache[0]