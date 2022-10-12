class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rides.sort()
        total_rides = len(rides)
        
        def next_index(idx):

            curr_end = rides[idx][1]
            l, h = idx + 1, total_rides - 1

            while l <= h:
                mid = (l+h) // 2
                if rides[mid][0] < curr_end:
                    l = mid + 1
                elif rides[mid][0] > curr_end:
                    h = mid - 1
                else:
                    h = mid - 1

            return l


        def calculate_profit(idx):
            return rides[idx][1] - rides[idx][0] + rides[idx][2]


        cache = [-1] * (total_rides+1)
        def solve(idx):

            if idx >= total_rides: return 0
            if cache[idx] != -1: return cache[idx]

            pick = calculate_profit(idx) + solve(next_index(idx))
            not_pick = solve(idx+1)

            cache[idx] = max(pick, not_pick)
            return cache[idx] 


        return solve(0)