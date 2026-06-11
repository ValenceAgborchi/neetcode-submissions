class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = {}

        for idx, num in enumerate(nums):
            diff = target - num
            if diff in output:
                return [output[diff], idx]
            output[num] = idx
        
        return output
      
