class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ourmap = {}
        for index, num in enumerate(nums):
            difference = target - num
            if difference in ourmap:
                return [ourmap[difference], index]
            ourmap[num] = index
            
        
            

