class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #O(nlogn) solution

        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        
        return False




        
