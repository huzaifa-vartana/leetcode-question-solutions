class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        edges = {}
        max_freq = 0

        N = len(wall)

        for row in range(N):
            current_bricks = wall[row]

            current_bricks_length = 0
            for idx, brick in enumerate(current_bricks):
                if idx == len(current_bricks) - 1:
                    continue

                current_bricks_length += brick
                edges[current_bricks_length] = edges.get(
                    current_bricks_length, 0) + 1

                max_freq = max(max_freq, edges[current_bricks_length])

        return len(wall) - max_freq
