class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        index1 = 1
        right = len(numbers) - 1
        index2 = len(numbers)

        while left < right:
            if numbers[left] + numbers[right] > target:
                right -= 1
                index2 -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
                index1 += 1
            else:
                return [index1, index2]
  
        return []