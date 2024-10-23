from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        N = len(people)
        people = sorted(people)
        k = 2
        boats = 0

        i, j = 0, N - 1
        while i <= j:
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
            boats += 1

        return boats
