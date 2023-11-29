class Solution:
    def distance_fn(self, x: int, y: int) -> int:
        return x ** 2 + y ** 2
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = [(-self.distance_fn(*points[0]), points[0])]

        for point in points[1:]:
            curr_dist = self.distance_fn(*point)
            if len(max_heap) < k:
                heapq.heappush(max_heap, (-curr_dist, point))
            elif max_heap[0][0] < curr_dist:
                heapq.heappushpop(max_heap, (-curr_dist, point))
        
        return [x[1] for x in max_heap]