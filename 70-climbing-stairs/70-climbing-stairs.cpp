class Solution {
public:
    int climbStairs(int n) {
        if (n < 4) {
            return n;
        }
        
        int prev = 0, fib = 1;
        int _sum;
        for (int i = 0; i < n; i++) {
            _sum = prev + fib;
            prev = fib;
            fib = _sum;
        }
        return fib;
    }
};