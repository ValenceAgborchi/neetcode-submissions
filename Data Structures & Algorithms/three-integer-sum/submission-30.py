class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        sortednums = sorted(nums)

        for i in range(len(sortednums)):
            if i > 0 and sortednums[i] == sortednums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = sortednums[i] + sortednums[left] + sortednums[right]

                if total == 0:
                    output.append([sortednums[i], sortednums[left], sortednums[right]])
                    left += 1
                    right -= 1
                    while left < right and sortednums[left] == sortednums[left - 1]:
                        left += 1
                    while left < right and sortednums[right] == sortednums[right + 1]:
                        right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
            
        return output
                
            
            
            

  
        


