class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ocurrences = {}

        for i in range(len(nums)):
            ocurrences[nums[i]] = 1 + ocurrences.get(nums[i], 0)
        
        heap = []

        for num, cnt in ocurrences.items():
            heapq.heappush(heap, [cnt, num])
            while len(heap) > k:
                heapq.heappop(heap)    

        output = []

        while len(output) < k:
            output.append(heap.pop()[1])
        
        return output


        
