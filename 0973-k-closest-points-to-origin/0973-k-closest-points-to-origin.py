class Solution:
    def distance_fn(self, point: List[int]) -> int:
        return point[0] ** 2 + point[1] ** 2
    
    def kClosest_maxheap(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Using max-heaps takes about O(Nlogk).
        max_heap = [(-self.distance_fn(points[i]), points[i]) for i in range(k)]
        heapq.heapify(max_heap)
        
        for i in range(k, len(points)):
            curr_dist = self.distance_fn(points[i])
            if max_heap[0][0] < curr_dist:
                heapq.heappushpop(max_heap, (-curr_dist, points[i]))
        
        return [x[1] for x in max_heap]
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Using min-heaps takes about O(N + KlogN).
        min_heap = [(self.distance_fn(pt), pt) for pt in points]
        heapq.heapify(min_heap)
        
        k_closest = [heapq.heappop(min_heap)[1] for _ in range(k)]
        return k_closest