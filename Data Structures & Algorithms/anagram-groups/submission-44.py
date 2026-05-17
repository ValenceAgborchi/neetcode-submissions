class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ourmap = defaultdict(list)
        for i in strs:
            sortedstring = sorted(i)
            #A sorted string returns a '' seperated list, so your dictionary key must be a tuple
            #Unless you ''.join(sorted(i))
            ourmap[tuple(sortedstring)].append(i)
        return list(ourmap.values())