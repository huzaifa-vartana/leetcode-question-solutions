class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        ones = students.count(1)
        zeros = students.count(0)


        for idx, sandwich in enumerate(sandwiches):
            if sandwich == 0:
                zeros -= 1
            else:
                ones -= 1

            if zeros < 0 or ones < 0: 
                return len(sandwiches) - idx
        # print(sandwich, ones, zeros)
        return 0