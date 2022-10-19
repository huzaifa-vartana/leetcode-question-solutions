#User function Template for python3
from functools import lru_cache
class Solution:
    def matrixMultiplication(self, N, arr):
        
        n = len(arr)
        
        cache = [[0 for _ in range(n-1)] for _ in range(n-1)]
        for gap in range(n):
            i, j = 0, gap
            while j < n-1:
                
                if gap == 0:
                    cache[i][j] = 0
                elif gap == 1:
                    cache[i][j] = arr[i] * arr[i+1] * arr[j+1]
                else:
                    mini = float('inf')
                    for k in range(i, j):
                        mini = min(
                            mini,
                            cache[i][k] + cache[k+1][j] + arr[i] * arr[k+1] * arr[j+1]
                            )
                    
                
                    cache[i][j] = mini
                j +=1
                i += 1
        return cache[0][-1]

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