class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = {}

        for i in range(len(nums)):
            output[nums[i]] = 1 + output.get(nums[i], 0)
        
        heap = []
        for num, cnt in output.items():
            heapq.heappush(heap, [cnt, num])
            while len(heap) > k:
                heapq.heappop(heap)


        res = []

        while len(res) < k:
            res.append(heap.pop()[1])
        
        return res