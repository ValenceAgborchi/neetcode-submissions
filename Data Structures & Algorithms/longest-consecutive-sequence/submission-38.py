class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)   
        result = 0

        for i in nums:
            count = 0
            if i in store:
                count += 1
                while i + count in store:
                    count += 1
                result = max(result, count)
        return result

                    





        
   
      





        