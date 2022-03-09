class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]
        
        even = False
        _append = ans.append  # for time imp.
        for i in range(1, n + 1):
            if even:
                _append(ans[i // 2])
            else:
                _append(ans[-1] + 1)
            even = ~even
            
        return ans