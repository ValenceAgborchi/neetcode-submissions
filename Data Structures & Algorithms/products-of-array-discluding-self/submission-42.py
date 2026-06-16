class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # BruteForce O(n^2) Solution
        output = [1] * len(nums)

        for i in range(len(nums)):
            num = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                num *= nums[j]

            output[i] *= num
        
        return output
     