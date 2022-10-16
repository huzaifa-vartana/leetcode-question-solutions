#User function Template for python3
from functools import lru_cache
class Solution:
    def matrixMultiplication(self, N, arr):
        

        
        
        n = len(arr)
        cache = [[0 for _ in range(n+2)] for _ in range(n+2)]
        
        for i in range(n-1, -1, -1):
            for j in range(i+1, n-1):
                mini = float('inf')
                if i >= j:
                    continue
        
                for k in range(i, j):
                    mini = min(
                        mini,
                        cache[i][k] + cache[k+1][j] + arr[i] * arr[k+1] * arr[j+1]
                    )
        
                cache[i][j] = mini
                
        return cache[0][n-2]


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