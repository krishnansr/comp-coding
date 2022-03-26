class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        pair_arr = [0] * 2001
        for i in arr:
            _match = (i >= 0) - (i < 0)
            if pair_arr[2 * i] == _match or (not i & 1 and pair_arr[i // 2] == _match):
                return True
            pair_arr[i] = _match
        return False