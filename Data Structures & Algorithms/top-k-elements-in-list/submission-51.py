class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ourmap = defaultdict(list)

        for i in nums:
            ourmap[i] = 1 + ourmap.get(i, 0)
        
        heap = []
        for num, count in ourmap.items():
            heapq.heappush(heap, [count, num])
            if len(heap) > k:
                heapq.heappop(heap)
              

        result = []
        while len(result) < k:
            result.append(heapq.heappop(heap)[1])
        return result
 
        



        
        

