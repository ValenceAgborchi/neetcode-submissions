class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ourlist = defaultdict(list)

        for i in strs:
            s = sorted(i)
            ourlist[tuple(s)].append(i)
        
        return list(ourlist.values())





