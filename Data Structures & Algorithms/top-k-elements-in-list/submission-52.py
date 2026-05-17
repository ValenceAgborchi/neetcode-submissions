class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ourmap = defaultdict(int)

        for i in nums:
            ourmap[i] = 1 + ourmap.get(i, 0)
        
        arr = []
        for num, cnt in ourmap.items():
            arr.append([cnt, num])
        arr.sort()

        result = []

        while len(result) < k:
            result.append(arr.pop()[1])
        
        return result
        

