class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #BRUTEFORCE O(N^2)
        
        store = set(nums)
        result = 0


        for i in nums:           
            current = i
            count = 0
            while current in store:
                count += 1
                current += 1
            result = max(result, count)
        
        return result






        