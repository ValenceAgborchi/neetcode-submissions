class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ocurrences = {}

        for i in range(len(nums)):
            ocurrences[nums[i]] = 1 + ocurrences.get(nums[i], 0)
        
        valuesortedarr = []

        for num, cnt in ocurrences.items():
            valuesortedarr.append([cnt, num])
        valuesortedarr.sort()

        output = []

        while len(output) < k:
            output.append(valuesortedarr.pop()[1])
        
        return output


        
