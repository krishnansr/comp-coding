class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        pair_arr = [0] * 2001
        for i in arr:
            if i > 0:
                if pair_arr[2 * i] == 1:
                    return True
                if not i & 1:
                    if pair_arr[i // 2] == 1:
                        return True
                pair_arr[i] = 1
            elif i < 0:
                i = abs(i)
                if pair_arr[2 * i] == 2:
                    return True
                if not i & 1:
                    if pair_arr[i // 2] == 2:
                        return True
                pair_arr[i] = 2
            else:
                pair_arr[0] += 1
                if pair_arr[0] > 1:
                    return True
        return False