class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0 
        index1 = left + 1
        right = len(numbers) - 1
        index2 = right + 1

        while left < right:
            oursum = numbers[left] + numbers[right]
            if oursum > target:
                right -= 1
                index2 -= 1
            elif oursum < target:
                left += 1
                index1 += 1
            else:
                return [index1, index2]
        return []
            
        