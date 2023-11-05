class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Time complexity: O(Nlogk)
        heap = nums[:k]
        heapq.heapify(heap)  # It's a min-heap, contains k largest elements.
        
        for n in nums[k:]:
            if n > heap[0]:  # n is greater than the smallest of k largest elements.
                heapq.heappushpop(heap, n)
        return heap[0]  # the smallest of the k largest elements
    
    def findKthLargest_quickselect(self, nums: List[int], k: int) -> int:
        # using quickSelect, O(n) time complexity on average,
        # O(N^2) time complexity in the worst case
        # TLE exception for huge arrays (due to nature of quick select)
        return self.findKthLargest_pt(nums, k, 0, len(nums) - 1)
        
    def findKthLargest_pt(self, nums: List[int], k: int, st: int, end: int) -> int:
        if k == 1:
            return nums[st]
        
        pivot_ind = self.partition(nums, st, end)

        left_size = pivot_ind - st  # smaller elements
        right_size = end - pivot_ind  # larger elements
        
        # print(k, nums, st, end, pivot_ind)
        nth_largest = end - pivot_ind + 1 # current pivot is the nth largest
        # print(nth_largest, left_size, right_size)
        if k == nth_largest:
            return nums[pivot_ind]
        elif k <= right_size:
            return self.findKthLargest_pt(nums, k, pivot_ind + 1, end)
        else:
            return self.findKthLargest_pt(nums, k - nth_largest, st, pivot_ind - 1)

    def partition(self, nums: List[int], low: int, high: int) -> int:
        pivot = nums[high]
        i = low - 1
        
        for j in range(low, high):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]

        nums[i + 1], nums[high] = nums[high], nums[i + 1]
        return i + 1