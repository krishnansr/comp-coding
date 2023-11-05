class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums[:k]
        heapq.heapify(self.heap)  # It's a min-heap, contains k largest elements.

        for n in nums[k:]:
            if n > self.heap[0]:
                # n is greater than the smallest of k largest elements.
                heapq.heappushpop(self.heap, n)
        
    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            # val is greater than the smallest of k largest elements.
            heapq.heappushpop(self.heap, val)

        return self.heap[0]  # the smallest of the k largest elements.


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)