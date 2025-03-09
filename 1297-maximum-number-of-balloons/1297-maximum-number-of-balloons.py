class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        count = Counter(text)
        needed = Counter("balloon")
        
        res = float('inf')
        for char in needed.keys():
            res = min(res, count[char] // needed[char])

        return res

            
        