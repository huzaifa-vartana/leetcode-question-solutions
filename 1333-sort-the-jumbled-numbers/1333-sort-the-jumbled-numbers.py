class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:

        ans = []
        for i, num in enumerate(nums):
            mapped_num = ""
            num = str(num)
            for n in num:
                mapped_num += str(mapping[int(n)])

            ans.append((int(mapped_num), i))

        ans.sort()
        return [nums[i] for (_, i) in ans]
        