class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
   

        result = defaultdict(list)

        for i in strs:
            sorteds = ''.join(sorted(i))
            result[sorteds].append(i)
            
        return list(result.values())


  


            