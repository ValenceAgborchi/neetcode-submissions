class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)
        res = 0
        
        for i in range(len(nums)):
            count = 0
            current = nums[i]
            if nums[i] in store:
                count += 1
                current += 1
                while current in store:
                    current += 1
                    count += 1
                res = max(res, count)
        return res
                
                    





        
   
      





        