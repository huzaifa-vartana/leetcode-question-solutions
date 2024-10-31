class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        if not digits: return []
        output = []

        def helper(idx, res):

            if idx >= len(digits): 
                output.append(res)
                return

            for letter in digit_to_letters[digits[idx]]:
                helper(idx+1, res + letter)


        helper(0, "")
        return output