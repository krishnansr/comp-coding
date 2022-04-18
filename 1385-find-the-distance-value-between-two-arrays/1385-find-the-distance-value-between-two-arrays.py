class Solution:
    @staticmethod
    def isValid(x1, arr2, d):
        l, r = 0, len(arr2) - 1

        while l <= r:
            mid = (l + r) // 2
            if abs(arr2[mid] - x1) <= d:
                return False
            elif x1 < arr2[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return True
    
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        
        return sum([self.isValid(x1, arr2, d) for x1 in arr1])
    
    
    def findTheDistanceValueBrute(self, arr1: List[int], arr2: List[int], d: int) -> int:
        return sum([all([ abs(x1 - x2) > d for x2 in arr2]) for x1 in arr1])