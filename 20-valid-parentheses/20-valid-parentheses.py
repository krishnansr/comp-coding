class Solution:
    brack_map = {'(': ')', '[': ']', '{': '}'}
    
    def isValid(self, s: str) -> bool:
        stack_count = list()
        for _char in s:
            if _char in self.brack_map:
                stack_count.append(_char)
            elif not len(stack_count) or self.brack_map[stack_count.pop()] != _char:
                return False
        return not len(stack_count)