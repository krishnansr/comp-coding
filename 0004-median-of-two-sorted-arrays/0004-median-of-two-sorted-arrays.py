class Solution:
    # def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

    def findMedianSortedArrays(self, X: List[int], Y: List[int]) -> float:
        m, n = len(X), len(Y)
        if m > n:
            X, Y, m, n = Y, X, n, m  # swap arrays

        i_min, i_max, half_len = 0, m, (m + n + 1) // 2
        while i_min <= i_max:
            i = (i_min + i_max) // 2
            j = half_len - i
            if i < m and Y[j-1] > X[i]:
                i_min = i + 1
            elif i > 0 and X[i-1] > Y[j]:
                i_max = i - 1
            else:
                if i == 0:
                    max_of_left = Y[j-1]
                elif j == 0: 
                    max_of_left = X[i-1]
                else: 
                    max_of_left = max(X[i-1], Y[j-1])
                
                if (m + n) % 2 == 1:
                    return max_of_left
                
                if i == m: 
                    min_of_right = Y[j]
                elif j == n: 
                    min_of_right = X[i]
                else: 
                    min_of_right = min(X[i], Y[j])
                
                return (max_of_left + min_of_right) / 2