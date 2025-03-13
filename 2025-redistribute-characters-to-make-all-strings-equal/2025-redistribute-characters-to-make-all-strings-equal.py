class Solution:
    def makeEqual(self, words: List[str]) -> bool:

        ctr = dict()

        for word in words:
            for char in word:
                ctr[char] = ctr.get(char, 0) + 1

        for char, freq in ctr.items():
            if freq % len(words) != 0: return False

        return True
        