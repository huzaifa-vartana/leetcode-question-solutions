class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        intervals = sorted(intervals)

        max_rooms = 0
        max_rooms_list = []
        if intervals:
            heapq.heappush(max_rooms_list, (intervals[0][1], intervals[0][0]))
            max_rooms = 1
        for start, end in intervals[1:]:
            earliest_meeting_ending = heapq.heappop(max_rooms_list)
            if start < earliest_meeting_ending[0]:
                heapq.heappush(max_rooms_list, earliest_meeting_ending)
                heapq.heappush(max_rooms_list, (end, start))
            else:
                heapq.heappush(max_rooms_list, max(
                    earliest_meeting_ending, (end, start)))

            max_rooms = max(max_rooms, len(max_rooms_list))
        return max_rooms



