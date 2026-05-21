class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        leftidx = 1
        rightidx = len(numbers)


        while left < right:
            oursum = numbers[left] + numbers[right]
            if oursum > target:
                right -= 1
                rightidx -= 1
            
            if oursum < target:
                left += 1
                leftidx += 1

            if oursum == target:
                return [leftidx, rightidx]

        return []
            
       