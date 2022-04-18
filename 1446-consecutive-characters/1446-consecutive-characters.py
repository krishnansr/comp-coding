class Solution:
    def maxPower(self, s: str) -> int:
        power, count, prev = 1, 1, s[0]
        for _char in s[1:]:
            if _char == prev:
                count += 1
            else:
                prev = _char
                power = max(power, count)
                count = 1
        return max(power, count)