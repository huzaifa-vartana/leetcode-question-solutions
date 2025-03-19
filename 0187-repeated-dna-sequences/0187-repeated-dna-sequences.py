class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        repeated = defaultdict(int)
        output = []
        left = 0
        for right in range(9, len(s)):
            repeated[s[left:right+1]] += 1

            if repeated[s[left:right+1]] == 2:
                output.append(s[left:right+1])

            left += 1

        return output