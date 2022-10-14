class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        n, m = len(board), len(board[0])
        def valid(x, y): return x >= 0 and x < n and y >= 0 and y < m
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        len_ = len(word)
        

        def solve(i, j, idx):
            if idx >= len_: return True
            tmp = board[i][j]
            board[i][j] = -1
            
            
            for dx, dy in directions:
                nr, nc = dx+i, dy+j
                if not valid(nr, nc) or board[nr][nc] == -1: continue
                if word[idx] == board[nr][nc] and solve(nr, nc, idx+1): return True
            
            board[i][j] = tmp
            return False
        
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0] and solve(i, j, 1): return True
                
        
        return False