class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        N = len(nums)
        ctr = Counter(nums)
        max_ = 0

        for num in ctr.keys():
            if num-1 in ctr: continue
            count = 1
            while num+count in ctr:
                count += 1

            max_ = max(max_, count)


        return max_
    
    