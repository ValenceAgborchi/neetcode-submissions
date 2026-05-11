
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        amap = {}

        for i in nums:
            amap[i] = amap.get(i, 0) + 1
        
        heap = []

        for key, value in amap.items():
            # Popping from minheap when the length goes over k allows us to end with the top k values
            heapq.heappush(heap, [value, key])
            if len(heap) > k:
                heapq.heappop(heap)
        
        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        
        return result

        
        

        



    


        



        
        


            



 