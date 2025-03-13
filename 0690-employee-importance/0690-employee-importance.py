"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emp = {employee.id: employee for employee in employees}

        def dfs(employee):
            importance = employee.importance
            for subordinate in employee.subordinates:
                importance += dfs(emp[subordinate])

            return importance
        return dfs(emp[id])
        