class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #RUNTIME here is O(NLOGN) due to sorting, but can be improved to O(N) by iterating and using a hashmap to count ocurrences
        if len(s) != len(t):
            return False
        
        return sorted(s) == sorted(t)
      


        

    