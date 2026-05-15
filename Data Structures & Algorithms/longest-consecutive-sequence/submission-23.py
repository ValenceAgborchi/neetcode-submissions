class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)
        res = 0
        for i in range(len(nums)):
            if nums[i] - 1 not in store:
                length = 1
                current = nums[i]
                while nums[i] + length in store:
                    length += 1
                    current += 1
                res = max(res, length)
        return res

        
   
      





        