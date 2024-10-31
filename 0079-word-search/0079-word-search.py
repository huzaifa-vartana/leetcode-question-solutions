from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        N, M = len(board), len(board[0])
        WORD_LEN = len(word)

        def helper(i, j, word_idx):
            if word_idx >= WORD_LEN:
                return True

            for x, y in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                i_, j_ = i + x, j + y

                if i_ < 0 or i_ >= N or j_ < 0 or j_ >= M:
                    continue
                if board[i_][j_] == "X":
                    continue
                if word[word_idx] != board[i_][j_]:
                    continue

                tmp = board[i][j]
                board[i][j] = "X"
                if helper(i_, j_, word_idx + 1):
                    return True
                board[i][j] = tmp

            return False

        for i in range(N):
            for j in range(M):
                if board[i][j] == word[0] and helper(i, j, 1):
                    return True

        return False

