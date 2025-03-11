class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ctr = {}
        good_pairs = 0

        for idx, num in enumerate(nums):
            if num in ctr:
                good_pairs += ctr[num]
                ctr[num] += 1
            else:
                ctr[num] = 1
        print(ctr)

        return good_pairs

        