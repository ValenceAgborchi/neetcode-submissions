class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       if len(s) != len(t):
            return False
        
       counts, tcount = {},{}

       for i in range(len(s)):
            counts[s[i]] = 1 + counts.get(s[i], 0)
            tcount[t[i]] = 1 + tcount.get(t[i], 0)

       return counts == tcount
        

    