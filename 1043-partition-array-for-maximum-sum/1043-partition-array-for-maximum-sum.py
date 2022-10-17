class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], max_length: int) -> int:
        
        
        n = len(arr)
        cache = [float('-inf')] * (n+1)
        cache[n] = 0
        for idx in range(n-1, -1, -1):
                        
            maxi = float('-inf')
            for k in range(idx, min(idx+max_length, n)):
                tmp = max(arr[idx:k+1]) * (k - idx + 1)
                maxi = max(
                    maxi,
                    tmp + cache[k+1]
                )
            cache[idx] = maxi

        return cache[0] 