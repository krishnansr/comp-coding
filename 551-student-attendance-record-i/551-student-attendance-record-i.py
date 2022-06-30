class Solution:
    def checkRecord(self, s: str) -> bool:
        return not re.search( r"A.*A|L{3,}", s)