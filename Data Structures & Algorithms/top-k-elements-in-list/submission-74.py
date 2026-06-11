class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = {}

        for i in range(len(nums)):
            output[nums[i]] = 1 + output.get(nums[i], 0)
        
        arr = []
        for num, cnt in output.items():
            arr.append([cnt, num])
        arr.sort()

        res = []

        while len(res) < k:
            res.append(arr.pop()[1])
        
        return res