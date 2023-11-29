class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Very similar to Applied inuition question. 
        # Can be solved in O(log N + k) time using binary search.
        # Template solution here: https://leetcode.com/problems/find-k-closest-elements/discuss/106426/JavaC%2B%2BPython-Binary-Search-O(log(N-K)-%2B-K)
        
        l, r = 0, len(arr) - k
        while l < r:
            mid = (l + r) // 2
            if x - arr[mid] > arr[mid + k] - x:
                l = mid + 1
            else:
                r = mid
                
        # So the main idea of it is to find out the lower bound of that k length range. The numbers between "left" and "right" are the candidates of the lower bound.
        # The if condition "x - A[mid] > A[mid + k] - x" is used to compare A[mid] and A[mid+k], see which is closer to x.
        # If A[mid] is closer to x, then A[mid+k] can never be in the k length range. So we can confidently remove all (A[mid+1], A[mid+2], A[mid+3]...) from the candidates list by set right=mid.
        # If A[mid+k] is closer to x, then A[mid] can never be in the k length range. So we can confidently remove all (...A[mid-2], A[mid-1], A[mid]) from the candidates list by set left=mid+1.
        # Once we remain only one candidate, that is left==right, we got our final lower bound.
        return arr[l: l + k]