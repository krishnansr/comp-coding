class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]
    
        _append = ans.append  # for time imp.
        for i in range(1, n + 1):
            if i%2 == 0:
                _append(ans[i // 2])
            else:
                _append(ans[-1] + 1)
        return ans