class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 0 
        ourset = set(nums)
        result = 0

        for i in nums:
       
            if i - 1 not in ourset:

                streak = 1

                while i + streak in ourset:
                    streak += 1
                result = max(result, streak)
        return result




        
   
      





        