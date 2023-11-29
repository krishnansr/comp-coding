class Solution:
    def distance_fn(self, x: int, y: int) -> int:
        return x ** 2 + y ** 2
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Using heaps takes about O(Nlogk)
        max_heap = [(-self.distance_fn(*points[i]), points[i]) for i in range(k)]
        heapq.heapify(max_heap)
        
        for i in range(k, len(points)):
            curr_dist = self.distance_fn(*points[i])
            if max_heap[0][0] < curr_dist:
                heapq.heappushpop(max_heap, (-curr_dist, points[i]))
        
        return [x[1] for x in max_heap]