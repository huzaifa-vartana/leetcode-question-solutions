from typing import List
from collections import deque


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = Counter(students)
        eaten = 0 

        for sandwich in sandwiches:
            if count[sandwich] > 0:
                count[sandwich] -= 1
                eaten += 1
            else:
                return len(sandwiches) - eaten

        return len(sandwiches) - eaten

