class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        ans = 0

        counter = Counter(tasks)
        for key, freq in counter.items():
            if freq == 1:
                return -1

            ans += (freq + 2) // 3
            


        return ans