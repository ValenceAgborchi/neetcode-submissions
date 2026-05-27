class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            left = 0
            right = len(i) - 1

            while left <= right:
                middle = (left + right) // 2
                if i[middle] > target:
                    right = middle - 1
                elif i[middle] < target:
                    left = middle + 1
                else:
                    return True
        return False
                