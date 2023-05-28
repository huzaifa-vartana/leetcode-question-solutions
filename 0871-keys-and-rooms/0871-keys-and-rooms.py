class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        seen = set()
        def dfs(key):
            seen.add(key)

            for nei in rooms[key]:
                if nei not in seen:
                    dfs(nei)


        dfs(0)
        return len(seen) == len(rooms)