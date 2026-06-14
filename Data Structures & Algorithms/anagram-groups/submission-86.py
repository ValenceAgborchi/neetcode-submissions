class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupedlist = defaultdict(list)

        for i in strs:
            sortedstring = sorted(i)
            groupedlist[tuple(sortedstring)].append(i)
        
        return list(groupedlist.values())