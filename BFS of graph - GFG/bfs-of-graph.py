#User function Template for python3
from collections import deque

class Solution:
    
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V, adj):
        
        
        q = [0]
        ans = []
        
        seen = set()
        seen.add(0)
        while q:
            node = q.pop(0)
            ans.append(node)
            for nei in adj[node]:
                if nei not in seen:
                    q.append(nei)
                    seen.add(nei)
        
        
        
        
        return ans
        


#{ 
 # Driver Code Starts

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends