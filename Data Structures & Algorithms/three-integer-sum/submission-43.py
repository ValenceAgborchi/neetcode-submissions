class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        sorteds = sorted(nums)
        for i in range(len(sorteds)):
            if i > 0 and sorteds[i] == sorteds[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = sorteds[i] + sorteds[left] + sorteds[right]

                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    output.append([sorteds[i], sorteds[left], sorteds[right]])
                    left += 1
                    right -= 1

                    while left < right and sorteds[left] == sorteds[left - 1]:
                        left += 1
                    while left < right and sorteds[right] == sorteds[right + 1]:
                        right -= 1

        return output
            


            
       