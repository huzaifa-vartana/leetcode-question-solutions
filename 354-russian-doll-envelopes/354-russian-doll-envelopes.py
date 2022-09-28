class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        
        envelopes.sort(key = lambda x: [x[0], -x[1]])
        n = len(envelopes)

        def bs(nums, key):
            low, high = 0, len(nums) - 1
            while low <= high:
                mid = (low+high) // 2
                if nums[mid] == key:
                    return mid
                if nums[mid] > key:
                    high = mid - 1
                else:
                    low = mid + 1

            return low
        
        
        res = [envelopes[0][1]]
        for idx in range(1, n):
            if envelopes[idx][1] > res[-1]:
                res.append(envelopes[idx][1])
            else:
                res[bs(res, envelopes[idx][1])] = envelopes[idx][1]
                
        return len(res)
        
        