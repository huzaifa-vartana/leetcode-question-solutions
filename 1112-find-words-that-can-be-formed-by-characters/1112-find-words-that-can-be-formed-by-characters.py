class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_counter = Counter(chars)

        res = 0
        for word in words:
            word_counter = Counter(word)

            pos = True
            for char, freq in word_counter.items():
                if chars_counter[char] < freq:
                    pos = False
                    break
            if pos: res += len(word)
                


        return res