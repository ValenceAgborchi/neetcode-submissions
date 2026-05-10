class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ourmap = {}
        for i in nums:
            ourmap[i] = ourmap.get(i, 0) + 1
        
        heap = []
        for i in ourmap.keys():
            heapq.heappush(heap, [ourmap[i], i])
            if len(heap) > k:
                heapq.heappop(heap)
        
        result = []
        for i in range(k):
            result.append(heap.pop()[1])
        
        return result

  
        



        
        

