from collections import deque
from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students_q = deque(students)
        sandwiches_idx = 0
        students_processed = 0

        while True:
            if students_q[0] == sandwiches[sandwiches_idx]:
                students_q.popleft()
                sandwiches_idx += 1
                students_processed = 0
            else:
                students_q.append(students_q.popleft())
                students_processed += 1
                if students_processed == len(students_q):
                    break
            
            if sandwiches_idx == len(sandwiches):
                break

        return len(students_q)
