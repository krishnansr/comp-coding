class Solution:
    def reformatNumber(self, number: str) -> str:
        res = ''
        for num in number:
            if num in ' -':
                continue
            if len(res) % 4 == 3:
                res += f'-{num}'
            else:
                res += num
        
        if res[-2] == '-':
            res = f'{res[:-3]}-{res[-3]}{res[-1]}'
        return res