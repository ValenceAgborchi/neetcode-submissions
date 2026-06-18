class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #O(n log n solution) # 2

        return sorted(s) == sorted(t)

        
