class Solution:
    def isPathCrossing(self, path: str) -> bool:

        visited = set()
        dirs = {
            "N": [0, 1],
            "S": [0, -1],
            "E": [1, 0],
            "W": [-1, 0]
        }

        curr_ptr = (0, 0)
        visited.add(curr_ptr)
        for direction in path:
            curr_ptr = (curr_ptr[0] + dirs[direction][0], curr_ptr[1] + dirs[direction][1])

            if curr_ptr in visited:
                return True

            visited.add(tuple(curr_ptr))
        return False