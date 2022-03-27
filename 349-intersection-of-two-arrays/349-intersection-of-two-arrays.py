class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # intersection over set
        return set(nums1) & set(nums2)