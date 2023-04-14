#User function Template for python3
class Solution:

	def maxProduct(self,arr, n):
	    max_n, max_p = arr[0], arr[0]
        max_product = float("-inf")

        for idx in range(1, len(arr)):
            num = arr[idx]
    
            if num < 0:
                max_product = max(
                    max_product,
                    max_n * num,
                    # max_p * num
                )
                max_n = min(max_n, num)
            else:
                max_product = max(
                    max_product,
                    max_p * num,
                    # max_n * num
                )
                max_p = max(max_p, num)
    
        return max_product


#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends