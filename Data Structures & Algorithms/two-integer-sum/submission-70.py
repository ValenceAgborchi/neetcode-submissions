class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        amap = {}

        for i, num in enumerate(nums):
            difference = target - num
            if difference in amap:
                return [amap[difference], i]
            amap[num] = i
        
        return []
   