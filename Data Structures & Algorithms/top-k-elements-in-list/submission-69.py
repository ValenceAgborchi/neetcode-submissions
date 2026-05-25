class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = {}
        for i in nums:
            output[i] = 1 + output.get(i, 0)
        
        heap = []
        for num, cnt in output.items():
            heapq.heappush(heap, [cnt, num])
            while len(heap) > k:
                heapq.heappop(heap)

        answer = []
        while len(answer) < k:
            answer.append(heap.pop()[1])
        
        return answer


       