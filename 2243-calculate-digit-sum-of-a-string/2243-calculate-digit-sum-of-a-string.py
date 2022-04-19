class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            s = ''.join(map(str, [reduce(lambda x, y: int(x) + int(y), s[i: i+k]) 
                                        for i in range(0, len(s), k)]))
        return s