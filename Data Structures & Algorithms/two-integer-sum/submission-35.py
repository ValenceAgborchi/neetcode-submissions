class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ourmap = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in ourmap:
                return [ourmap[diff], i]
            
            ourmap[num] = i
        
        return []
