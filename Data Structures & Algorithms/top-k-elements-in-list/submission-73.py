class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ourmap = {}

        for i in range(len(nums)):
            ourmap[nums[i]] = 1 + ourmap.get(nums[i], 0)
        
        heap = []
        for num, count in ourmap.items():
            heapq.heappush(heap, [count, num])
            while len(heap) > k:
                heapq.heappop(heap)
        
        output = []
        while len(output) < k:
            output.append(heap.pop()[1])
        
        return output



            




   