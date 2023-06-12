class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        # def move_to_next_day(curr, day):
        #     start, end = curr + 1, len(days) - 1
        #     res = curr + 1
        #     while start <= end:
        #         mid = (start + end) // 2
        #         if days[mid] == days[curr] + day:
        #             res = mid
        #             start = mid + 1
        #         elif days[mid] > days[curr] + day:
        #             res = mid
        #             end = mid - 1
        #         else:
        #             res = mid
        #             start = mid + 1

        #     return res
        def move_to_next_day(curr, day):

            ptr = curr + 1
            while ptr < len(days) and days[curr] + day >= days[ptr]:
                ptr += 1

            return ptr

        cache = [-1] * (len(days)+1)            
        def solve(idx):

            # base cases
            if idx >= len(days): return 0
            if cache[idx] != -1: return cache[idx]

            # three recursive calls
            # case 1 - buy 1-day pass
            one_day_pass = costs[0] + solve(move_to_next_day(idx, 0))
            # case 2 - buy 7-day pass
            seven_day_pass = costs[1] + solve(move_to_next_day(idx, 6))
            # case 3 - buy 30-day pass
            thirty_day_pass = costs[2] + solve(move_to_next_day(idx, 29))

            # return mini
            cache[idx] = min(one_day_pass, seven_day_pass, thirty_day_pass)
            return cache[idx]



        return solve(0)
