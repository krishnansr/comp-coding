class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if letters[-1] <= target:
            return letters[0]
        
        left, right = 0, len(letters) - 1
        while left <= right:
            middle = (left + right) // 2
            
            if target >= letters[middle]:
                left = middle + 1
            else:
                right = middle - 1
        return letters[left]
        
    def nextGreatestLetter_scan(self, letters: List[str], target: str) -> str:
        if letters[-1] > target:
            for _char in letters:
                if _char > target:
                    return _char
        return letters[0]