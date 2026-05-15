class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 0 
        ourset = set(nums)
        result = 0

        for i in nums:
            #This conditional ensures we start at the smallest value in the streak
            if i - 1 not in ourset:
            #If i - 1 exists, we skip, ensuring only one iteration through array nums O(N^2)
                streak = 1
                #Start counting streak
                while i + streak in ourset:
                    streak += 1
                result = max(result, streak)
        return result




        
   
      





        