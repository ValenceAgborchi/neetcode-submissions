class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ourmap = {}

        for i in range(len(nums)):
            ourmap[nums[i]] = 1 + ourmap.get(nums[i], 0)
        
        arr = []
        for num, count in ourmap.items():
            arr.append([count, num])
        arr.sort()

        result = []
        while len(result) < k:
            result.append(arr.pop()[1])
        
        return result




   