
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ourmap = {}
        for num in nums:
            ourmap[num] = 1 + ourmap.get(num, 0)
        
        heap = []
        for j in ourmap.keys():
            heapq.heappush(heap, (ourmap[j], j))
            if len(heap) > k:
                heapq.heappop(heap)
        
        result = []

        for i in range(k):
            result.append(heap.pop()[1])
        
        return result
     

    


        



        
        


            



 