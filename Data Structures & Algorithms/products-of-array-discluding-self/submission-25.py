class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Bruteforce Solutoion using O(N^2) Time

        result = [1] * len(nums)

        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                else:
                    product *= nums[j]
            result[i] = product
                

        return result