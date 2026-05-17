class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ourmap = defaultdict(list)
        for i in strs:
            sortedstring = sorted(i)
            ourmap[tuple(sortedstring)].append(i)
        return list(ourmap.values())