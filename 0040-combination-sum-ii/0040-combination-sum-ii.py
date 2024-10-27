class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        output = []
        candidates.sort()

        def helper(idx, sum, res):
            if idx >= len(candidates):
                if sum == target: output.append(res)
                return 

            helper(idx+1, sum + candidates[idx], res + [candidates[idx]])
            while idx+1 < len(candidates) and candidates[idx] == candidates[idx+1]:
                idx += 1

            helper(idx+1, sum, res)
        


        helper(0, 0, [])
        return output