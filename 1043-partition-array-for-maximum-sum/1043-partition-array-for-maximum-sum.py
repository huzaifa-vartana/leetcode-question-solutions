class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], part: int) -> int:
        
        n = len(arr)

        @lru_cache(None)
        def partition(idx):

            if idx >= n: return 0

            max_sum = 0
            itr = min(idx + part, n)
            for k in range(idx, itr):

                subarray_sum = max(arr[idx:k+1]) * (k - idx + 1)
                max_sum = max(max_sum, subarray_sum + partition(k + 1))

            return max_sum
        
        return partition(0)