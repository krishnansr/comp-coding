class Solution:
    def arr_count(self, n: int) -> list:
        count_n = [0] * 10
        while n:
            count_n[n % 10] += 1
            n //= 10
        return count_n
    
    def reorderedPowerOf2(self, n: int) -> bool:
        count_n = self.arr_count(n)
        n = 1
        for _ in range(32):
            if count_n == self.arr_count(n):
                return True
            n<<=1
        return False