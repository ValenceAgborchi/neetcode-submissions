class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)

        for i in strs:
            lettercount = [0] * 26
            for j in i:
                lettercount[ord(j) - ord('a')] += 1
            output[tuple(lettercount)].append(i)
        
        return list(output.values())



        

        