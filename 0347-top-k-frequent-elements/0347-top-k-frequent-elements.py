class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = dict()
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        heap = [(-count, num) for num, count in counter.items()]
        heapq.heapify(heap)
        
        k_frequent = []
        for i in range(k):
            k_frequent.append(heapq.heappop(heap)[1])
        return k_frequent