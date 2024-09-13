from collections import defaultdict
from typing import Counter, List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_counter = defaultdict(int)

        words_formed_len = 0
        for char in chars:
            char_counter[char] += 1

        for word in words:
            word_counter = defaultdict(int)
            is_word_formed = True
            for char in word:
                word_counter[char] += 1
                if word_counter[char] > char_counter[char]:
                    is_word_formed = False
                    break

            if is_word_formed:
                words_formed_len += len(word)

        return words_formed_len