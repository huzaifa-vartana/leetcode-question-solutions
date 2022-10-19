#User function Template for python3
from functools import lru_cache
class Solution:
    def matrixMultiplication(self, N, arr):
        
        n = len(arr)
        
        @lru_cache(None)
        def solve(i, j):
            if i >= j: return 0
            
            mini = float('inf')
            for k in range(i, j):
                mini = min(
                    mini,
                    solve(i, k) + solve(k+1, j) + arr[i] * arr[k+1] * arr[j+1]
                    )
            
            return mini
            
        return solve(0, n-2)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        print(ob.matrixMultiplication(N, arr))
# } Driver Code Ends