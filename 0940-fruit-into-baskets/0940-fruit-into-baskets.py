class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        N = len(fruits)
        best, l = 0, 0
        count = {}
        for r in range(N):
            count[fruits[r]] = count.get(fruits[r], 0) + 1
            while len(count) > 2:
                count[fruits[l]] -= 1
                if count[fruits[l]] == 0:
                    del count[fruits[l]]
                l += 1
            best = max(best, r - l + 1)


        return best