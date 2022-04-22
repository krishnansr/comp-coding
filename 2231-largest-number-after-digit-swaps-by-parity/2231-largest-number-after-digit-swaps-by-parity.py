class Solution:
    def largestInteger(self, num: int) -> int:
        parity = []
        counter_ls = [[], []]

        while num > 0:
            _digit = num % 10
            counter_ls[_digit & 1].append(_digit)
            parity.insert(0, _digit & 1)
            num //= 10

        counter_ls[0].sort()
        counter_ls[1].sort()

        res = 0
        for par in parity:
            res = res * 10 + counter_ls[par].pop()

        return res