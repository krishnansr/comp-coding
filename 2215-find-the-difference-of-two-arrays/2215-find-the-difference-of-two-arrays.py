class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        counter = [0] * 2001

        for n in nums1:
            counter[n + 1000] = 1  # seen in arr 1
        
        for n in nums2:
            n += 1000
            if counter[n] == 1:
                counter[n] = -1  # in set intersection
            elif counter[n] == 0:
                counter[n] = 2  # seen in arr 2
                
        res = [[], []]
        for i, n in enumerate(counter):
            if n > 0 :
                res[n - 1].append(i - 1000)
        
        return res