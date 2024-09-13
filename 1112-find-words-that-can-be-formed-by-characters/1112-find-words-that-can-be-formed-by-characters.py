class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_counter = [0] * 26

        words_formed_len = 0
        for char in chars:
            char_counter[ord(char) - ord('a')] += 1

        for word in words:
            word_counter = [0] * 26
            for char in word:
                word_counter[ord(char) - ord('a')] += 1

            is_word_formed = True
            for i in range(26):
                if word_counter[i] > char_counter[i]:
                    is_word_formed = False
                    break

            if is_word_formed:
                words_formed_len += len(word)

        return words_formed_len

