class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        ileft = 1
        iright = len(numbers)


        while left < right:
            if numbers[left] + numbers[right] > target:
                right -= 1 
                iright -= 1
            if numbers[left] + numbers[right] < target:
                left += 1 
                ileft += 1
            if numbers[left] + numbers[right] == target:
                return [ileft, iright]
        
        return []
            