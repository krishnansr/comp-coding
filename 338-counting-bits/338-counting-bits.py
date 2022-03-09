class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]
        
        even = False
        for i in range(1, n + 1):
            if even:
                ans.append(ans[i // 2])
            else:
                ans.append(ans[-1] + 1)
            even = ~even
        return ans