class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        N = len(s)
        k = 10

        hash_map = defaultdict(int)
        res = []
        for char in range(N):
            hash_map[s[char:char+k]] += 1
            if hash_map[s[char:char+k]] == 2:
                res.append(s[char:char+k])

        return res