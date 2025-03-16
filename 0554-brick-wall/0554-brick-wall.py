class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        edges_map = defaultdict(int)

        total_gap = sum(wall[0])
        max_gaps = 0

        for row, bricks in enumerate(wall):
            bricks_length = 0
            for col, brick in enumerate(bricks):

                # dont want the last edge
                if col == len(bricks) - 1: continue

                bricks_length += brick
                edges_map[bricks_length] += 1

                max_gaps = max(max_gaps, edges_map[bricks_length])
            

        return len(wall) - max_gaps
