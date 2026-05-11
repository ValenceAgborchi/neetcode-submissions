class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        for index, num in enumerate(nums):
            diff = target - num
            if diff not in result:
                result[num] = index
            else:
                return [result[diff], index]
  

  


       