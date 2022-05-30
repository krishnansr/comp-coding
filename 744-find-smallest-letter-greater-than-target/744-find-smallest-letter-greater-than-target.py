class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if letters[-1] > target:
            for _char in letters:
                if _char > target:
                    return _char
        return letters[0]