class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        mod_s = ''
        i = 0
        while i < len(s):
            mod_s += s[i: i + k][::-1] + s[i + k: i + 2*k]
            i += 2 * k
        return mod_s