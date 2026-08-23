class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ourmap = {}
        for i, num in enumerate(nums):
            difference = target - num
            if difference in ourmap:
                return [ourmap[difference], i]
            ourmap[num] = i
        
        return []
