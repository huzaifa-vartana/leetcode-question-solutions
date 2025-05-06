class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def transform(point):
            distance = sqrt(point[0] ** 2 + point[1] ** 2)

            return (distance, (point[0], point[1]))

        heap = list(map(transform, points))
        heapq.heapify(heap)

        output = []
        while heap and k > 0:
            distance, (x, y) = heapq.heappop(heap)
            output.append([x, y])
            k -= 1

        return output
        
        