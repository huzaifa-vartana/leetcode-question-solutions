class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        m, n = len(image), len(image[0])
        starting_color = image[sr][sc]

        def valid(x, y): return x in range(0, m) and y in range(0, n)

        def dfs(i, j):

            if not valid(i, j): return
            image[i][j] = color

            for new_x, new_y in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
                if not valid(new_x, new_y): continue
                if image[new_x][new_y] != starting_color or image[new_x][new_y] == color: continue
                dfs(new_x, new_y)



        dfs(sr, sc)
        return image