class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)
        
        if (len1 + len2) & 1:  # odd length
            return self.kth_smallest(nums1, nums2, 0, len1 - 1, 0, len2 - 1, (len1 + len2) // 2)
        else:
            mid1 = self.kth_smallest(nums1, nums2, 0, len1 - 1, 0, len2 - 1, (len1 + len2) // 2)
            mid2 = self.kth_smallest(nums1, nums2, 0, len1 - 1, 0, len2 - 1, (len1 + len2) // 2 - 1)
            return (mid1 + mid2) / 2 
        
        
    def kth_smallest(self, nums1: List[int], nums2: List[int], st1: int, end1: int, st2: int, end2: int, k: int) -> float:
        # base cases are little tricky, check if st and end are still legal bounds
        # and use st1 for nums2, st2 for nums1 (swapped start positions)
        if st1 > end1:
            return nums2[k - st1]
        if st2 > end2:
            return nums1[k - st2]
    
        mid_ind1 = (st1 + end1) // 2
        mid_ind2 = (st2 + end2) // 2
        
        if nums1[mid_ind1] > nums2[mid_ind2]:  # swap so that A_mid <= B_mid
            nums1, nums2 = nums2, nums1
            st1, end1, st2, end2 = st2, end2, st1, end1
            mid_ind1, mid_ind2 = mid_ind2, mid_ind1
        
        
        # if sum of two median's indicies is smaller than k
        if (mid_ind1 + mid_ind2) < k:
            # can discard the left half of A because k is a large index, so it is unlikely to be in the left half of A
            return self.kth_smallest(nums1, nums2, mid_ind1 + 1, end1, st2, end2, k)
        else:
            # can discard the right haf of B, because k is a small index, so it unlikely to be in the right half of B
            return self.kth_smallest(nums1, nums2, st1, end1, st2, mid_ind2 - 1, k)

    
    
    def findMedianSortedArrays_no_rec(self, X: List[int], Y: List[int]) -> float:
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