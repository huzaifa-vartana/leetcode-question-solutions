class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        to = {}
        from_ = {}

        words = s.split(" ")
        if len(words) != len(pattern): return False

        for p, word in zip(pattern, words):
            if (p in to and to[p] != word) or (word in from_ and from_[word] != p): return False
            to[p] = word
            from_[word] = p


        return True