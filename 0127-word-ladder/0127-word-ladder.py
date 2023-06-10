class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:




        if beginWord == endWord: return 0
        if endWord not in wordList: return 0

        wordList = set(wordList)
        seen, q = set(), deque()

        seen.add(beginWord)
        q.append(beginWord)
        
        min_dis = 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                for c in 'qwertyuioplkjhgfdsazxcvbnm':
                    for idx in range(len(word)):
                        new_word = word[:idx] + c + word[idx+1:]
                        if new_word == endWord and new_word in wordList: return min_dis + 1

                        if new_word in seen or new_word not in wordList: continue
                        q.append(new_word)
                        seen.add(new_word)
            min_dis += 1

        return 0








