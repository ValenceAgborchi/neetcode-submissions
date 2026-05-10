
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        ourmap = {}
        for i in nums:
            ourmap[i] = 1 + ourmap.get(i, 0)
        
        heap = []
        for num in ourmap.keys():
            heapq.heappush(heap, (ourmap[num], num)) #Heaps compare FIRST tuple value

            if len(heap) > k:
                heapq.heappop(heap)
        
        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        
        return result



        
        


            



 