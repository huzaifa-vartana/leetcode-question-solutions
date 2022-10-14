class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], part: int) -> int:
        
        n = len(arr)
        cache = [-1 for _ in range(n+1)]
        
        
        def partition(idx):

            if idx >= n: return 0
            if cache[idx] != -1: return cache[idx]

            max_sum = 0
            itr = min(idx + part, n)
            for k in range(idx, itr):

                subarray_sum = max(arr[idx:k+1]) * (k - idx + 1)
                max_sum = max(max_sum, subarray_sum + partition(k + 1))

            cache[idx] = max_sum
            return cache[idx] 
        
        return partition(0)