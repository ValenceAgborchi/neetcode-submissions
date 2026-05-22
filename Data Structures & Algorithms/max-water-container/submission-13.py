class Solution:
    def maxArea(self, heights: List[int]) -> int:
         # BRUTEFORCE Checking every pairs height value using a nested loop
        output = 0
        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                base = j - i
                height = min(heights[i], heights[j])
                area = base * height
                output = max(output, area)
        return output





        