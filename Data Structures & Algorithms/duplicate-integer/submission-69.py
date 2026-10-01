class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ocurrences = set()
        for i in nums:
            if i in ocurrences:
                return True
            ocurrences.add(i)
        
        return False