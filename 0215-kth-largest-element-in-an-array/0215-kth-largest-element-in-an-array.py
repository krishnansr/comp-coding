class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)  # It's a min-heap, contains k largest elements.
        
        for n in nums[k:]:
            if n > heap[0]:  # n is greater than the smallest of k largest elements.
                heapq.heappushpop(heap, n)
        return heap[0]  # the smallest of the k largest elements