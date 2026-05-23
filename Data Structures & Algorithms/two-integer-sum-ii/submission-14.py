class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0 
        leftindex = 1
        right = len(numbers) - 1 
        rightindex = len(numbers)

        while left < right:
            total = numbers[left] + numbers[right]
            if total > target:
                right -= 1
                rightindex -= 1
            elif total < target:
                left += 1
                leftindex += 1
            
            else:
                return [leftindex, rightindex]
        return []


       