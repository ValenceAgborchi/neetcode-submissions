class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)
        res = 0
        
        for i in nums:
            if (i - 1) not in store:
                count = 1
                
                
                while (i + count) in store:
                
                    count += 1

                res = max(res, count)

        return res
                
                    





        
   
      





        