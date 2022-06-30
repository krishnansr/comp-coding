class Solution:
    def squareIsWhite(self, coords: str) -> bool:
        # return not (ord(coords[0]) - 97 + int(coords[1])) & 1
        return sum(map(ord, coords)) & 1