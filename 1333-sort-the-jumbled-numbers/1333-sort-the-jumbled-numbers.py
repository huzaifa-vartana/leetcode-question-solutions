class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:

        ans = []
        for i, num in enumerate(nums):
            mapped_num = 0
            if num == 0: mapped_num = mapping[0]

            """
            991
            1
            1

            1
            90

            900+91

            """

            base = 1
            while num > 0:
                last_digit = num % 10
                num //= 10
                mapped_num += base * mapping[last_digit]
                base *= 10
            
            print(mapped_num)

            ans.append((mapped_num, i))

        ans.sort()
        return [nums[i] for (_, i) in ans]
        