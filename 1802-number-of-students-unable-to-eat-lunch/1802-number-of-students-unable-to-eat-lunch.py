from typing import List
from collections import deque


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        sandwich_idx = 0
        students = deque(students)
        count = 0

        while students and count < len(students):
            if students[0] == sandwiches[sandwich_idx]:
                students.popleft()
                sandwich_idx += 1
                count = 0
            else:
                students.append(students.popleft())
                count += 1

            if sandwich_idx == len(sandwiches):
                break

        return len(sandwiches) - sandwich_idx
