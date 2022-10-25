class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)

        # cache = [[[-1 for _ in range(2)] for _ in range(n2+1)] for _ in range(n1+1)]
        cache = {}
        def solve(i, j, flag):
            state = (i, j, flag)
            if i == n1 or j == n2:
                # cache[i][j][flag] = float('-inf') if not flag else 0
                cache[state] = float('-inf') if not flag else 0
                # return cache[i][j][flag]
                return cache[state]
            # if cache[i][j][flag] != -1: return cache[i][j][flag]
            if state in cache: return cache[state]

            a = solve(i+1, j, flag)
            b = solve(i, j+1, flag)
            c = nums1[i] * nums2[j] + solve(i+1, j+1, True)
            d = solve(i+1, j+1, flag)

            # cache[i][j][flag] = max(a, b, c, d)
            # return cache[i][j][flag]
            cache[state] = max(a, b, c, d)
            return cache[state]
            
        
        
        
        return solve(0, 0, False)