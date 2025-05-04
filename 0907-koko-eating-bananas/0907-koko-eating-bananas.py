class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        ans = r

        while l <= r:
            k = (l+r) // 2
            possible = self.can_eat_all_bananas(piles, k, h)

            if possible:
                ans = k
                r = k - 1
            else:
                l = k + 1


        return ans

    def can_eat_all_bananas(self, piles, k, h):
        # check if k is possible
        hours = 0
        for pile in piles:
            hours += math.ceil(pile / k)
        return hours <= h