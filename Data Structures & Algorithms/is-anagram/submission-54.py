class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #O(n log n solution)

        if len(s) != len(t):
            return False
        
        sorteds = sorted(s)
        sortedt = sorted(t)
        
        for i in range(len(s)):
            if sorteds[i] != sortedt[i]:
                return False
        
        return True

        
