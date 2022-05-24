class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        pos_list, neg_list = [], []
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