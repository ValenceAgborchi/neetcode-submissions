class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += str(len(i)) + "#" + i
        return res

  
   

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            #Number between s[i] and s[j] (our delimiter) is our string length
            length = int(s[i:j])
            i = j + 1
            j = i + length
            #String between s[i] (First indice of string) to s[j] is the string
            res.append(s[i:j])
            i = j
        return res

            
     
        
     

        
        

