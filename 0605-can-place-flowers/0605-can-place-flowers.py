class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        N = len(flowerbed)

        for idx, val in enumerate(flowerbed):
            if val == 0:
                # middle flowers
                if idx+1 in range(N) and flowerbed[idx+1] == 0 and idx-1 in range(N) and flowerbed[idx-1] == 0:
                    flowerbed[idx] = 1
                    n -=1
                # corner cases
                if idx+1 not in range(N) and idx-1 in range(N) and flowerbed[idx-1] == 0:
                    flowerbed[idx] = 1
                    n -=1
                if idx+1 in range(N) and flowerbed[idx+1] == 0 and idx-1 not in range(N):
                    flowerbed[idx] = 1
                    n -=1

                if idx+1 not in range(N) and idx-1 not in range(N):
                    flowerbed[idx] = 1
                    n -=1

        return n <= 0
