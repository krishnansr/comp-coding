class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        l, r, i = 0, len(nums) - 1, len(nums) - 1
        
        while l <= r:
            left_val, right_val = abs(nums[l]), abs(nums[r])
            if left_val > right_val:
                res[i] = left_val ** 2
                l += 1
            else:
                res[i] = right_val ** 2
                r -= 1
            i -= 1  # to fill next biggest value
        return res
    
    def sortedSquares_extraspace(self, nums: List[int]) -> List[int]:
        pos_list, neg_list = [], []  # extra O(n) space
        for n in nums:
            if n < 0:
                neg_list.insert(0, n * n)
            else:
                pos_list.append(n * n)

        res, i, j = [], 0, 0
        while i < len(pos_list) and j < len(neg_list):
            if pos_list[i] < neg_list[j]:
                res.append(pos_list[i])
                i += 1
            else:
                res.append(neg_list[j])
                j += 1
        res.extend([*pos_list[i:], *neg_list[j:]])
        return res