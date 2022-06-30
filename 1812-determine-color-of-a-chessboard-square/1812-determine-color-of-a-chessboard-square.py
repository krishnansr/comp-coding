class Solution:
    def squareIsWhite(self, coords: str) -> bool:
        # a b c d e f g h
        # 0 1 2 3 4 5 6 7
        # odd - black, even white
        return not (ord(coords[0]) - 97 + int(coords[1])) & 1
