class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        for i in nums:
            hash[i]=hash.get(i, 0) + 1
        res = [[] for _ in range(len(nums)+1)]
        for i,j in hash.items():
            res[j].append(i)
        output = []
        for i in range(len(res)-1, k-1 , -1):
            # for i in 
            # print(res[i])
            for j in res[i]:
                output.append(j)
        print(output)
        return(output)
            
            
        