class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            count[i] = 1 + count.get(i, 0)
        
        heap = []
        for num, freq in count.items():
            heapq.heappush(heap, [freq, num])
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for i in range(k):
            res.append(heap.pop()[1])
        
        return res
