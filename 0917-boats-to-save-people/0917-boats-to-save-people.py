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
                l += 1
            r -= 1
            minn += 1

            
            
        return minn
        