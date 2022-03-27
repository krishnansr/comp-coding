class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        sol = [''] * n
        three, five = 3, 5
        
        for i in range(1, n+1):
            if i == three:
                sol[i-1] += 'Fizz'
                three += 3
            if i == five:
                sol[i-1] += 'Buzz'
                five += 5
            if not sol[i-1]:
                sol[i-1] = str(i)
        return sol
    
    def fizzBuzz_list_comp(self, n: int) -> List[str]:
        return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n+1)]