class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        N = len(people)
        people.sort()
        print(people)
        l, r = 0, N - 1
        minn = 0
        while l <= r:
            summ = people[l] + people[r]
            if summ <= limit: 
                minn += 1
                l += 1
                r -= 1
                continue

            if limit == people[l]:
                l += 1
            elif limit == people[r]:
                r -= 1
            elif people[r] >= people[l]:
                r -= 1
            elif people[l] > people[r]:
                l += 1
            minn += 1

            
            
        return minn
        