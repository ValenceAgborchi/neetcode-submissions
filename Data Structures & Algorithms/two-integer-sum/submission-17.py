class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        themap = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in themap:
                return [themap[diff], i]
            themap[num] = i
        return themap