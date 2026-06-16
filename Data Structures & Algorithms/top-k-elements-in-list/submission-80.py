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
        
        result = []
        while len(result) < k:
            result.append(heap.pop()[1])
        
        return result

