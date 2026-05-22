class Solution:
    def maxArea(self, heights: List[int]) -> int:
         #ptimal Solution in linear time using Two Pointers
        output = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            area = (right - left) * min(heights[left], heights[right])
            output = max(output, area)

            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        
        return output





        