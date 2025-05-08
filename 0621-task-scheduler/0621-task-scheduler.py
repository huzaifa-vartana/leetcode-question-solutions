class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # using priority queue
        counter = collections.Counter(tasks)
        max_heap = [-count for count in counter.values()]
        heapify(max_heap)
        cooldown = collections.deque()

        time = 0
        # using only 1 heap
        while max_heap or cooldown:
            time += 1
            if cooldown:
                # if the first element in the cooldown queue is ready to be added back to the heap
                if cooldown[0][0] == time:
                    heappush(max_heap, -cooldown.popleft()[1])

            if max_heap:
                # pop the most frequent task
                count = -heappop(max_heap)
                # if there are still tasks left, add it to the cooldown queue
                if count > 1:
                    cooldown.append((time + n + 1, count - 1))

        return time