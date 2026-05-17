class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #bruteforce runtime of O(N^2) here, but can be improved to O(N) by using hashmap to store indices of nums in list, and return when diff is in map
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                if nums[i] + nums[j] == target:
                    return [i, j]
        
            

