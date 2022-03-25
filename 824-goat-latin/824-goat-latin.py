class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        goat = ''
        vowels = set('aeiouAEIOU')
        
        for i, word in enumerate(sentence.split(' ')):
            if word[0] not in vowels:
                word = word[1:] + word[0]
            goat += f"{word}ma{'a' * (i + 1)} "
        
        return goat[:-1]