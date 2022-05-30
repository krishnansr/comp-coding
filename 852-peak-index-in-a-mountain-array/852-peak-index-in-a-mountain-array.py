class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1

        while left <= right:
            middle = (left + right) // 2

            if arr[middle - 1] < arr[middle]:
                if arr[middle] > arr[middle + 1]:
                    return middle
                left = middle + 1
            else:
                right = middle
                
        return -1