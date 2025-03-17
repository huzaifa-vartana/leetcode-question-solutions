class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:

        rectangle_ratios = defaultdict(int)
        count = 0
        
        for rectangle in rectangles:
            w, h = rectangle
            ratio = w / h
            count  += rectangle_ratios[ratio] * 1
            rectangle_ratios[ratio] += 1


        return count