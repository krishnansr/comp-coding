class Solution:
    digit_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                 '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    
    def letterCombinations(self, digits: str) -> List[str]:
        words = []
        if not digits:
            return words
        
        stack = [(0, '')]
        while stack:
            ind, curr_str = stack.pop()
            if ind == len(digits):
                words.append(curr_str)
            else:
                for _char in self.digit_map[digits[ind]]:
                    stack.append((ind + 1, curr_str + _char))
            
        return words