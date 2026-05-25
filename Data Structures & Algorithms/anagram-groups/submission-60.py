class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)

        for i in strs:
            sorteds = sorted(i)
            output[tuple(sorteds)].append(i)
        
        return list(output.values())
       