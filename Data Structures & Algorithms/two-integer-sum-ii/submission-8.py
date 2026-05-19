class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        leftindex = 1
        rightindex = len(numbers)

        while left < right:
            if numbers[left] + numbers[right] < target:
                left += 1
                leftindex += 1
            if numbers[left] + numbers[right] > target:
                right -= 1
                rightindex -= 1
            if numbers[left] + numbers[right] == target:
                return [leftindex, rightindex]
        
        return []


            