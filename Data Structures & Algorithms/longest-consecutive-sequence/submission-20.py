class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #BRUTEFORCE O(N^2)
        
   
        result = 0


        for i in nums:           
            current = i
            count = 0
            while current in nums:
                count += 1
                current += 1
            result = max(result, count)
        
        return result






        