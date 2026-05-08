class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        duplicate = False

        for i in nums:
            if i not in seen:
                seen.add(i)
            else:
                duplicate = True
        return duplicate
    
   
        