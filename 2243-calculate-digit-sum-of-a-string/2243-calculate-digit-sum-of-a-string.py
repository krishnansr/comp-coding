class Solution:
    def digitSum(self, s: str, k: int) -> str:
        if len(s) > k:
            new_s = ''.join(map(str, [reduce(lambda x, y: int(x) + int(y), s[i: i+k]) 
                                        for i in range(0, len(s), k)]))
        else:
            new_s = s
        return self.digitSum(new_s, k) if len(new_s) > k else new_s