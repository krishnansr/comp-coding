class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        count = [0] * 26
        for c in chain.from_iterable(words):
            count[ord(c) - 97] += 1
        
        for num in count:
            if num % len(words) != 0:
                return False
        return True