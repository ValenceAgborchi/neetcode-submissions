class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ourmap = defaultdict(list)

        for i in strs:
            sortedS = sorted(i)
            ourmap[tuple(sortedS)].append(i)
        
        return list(ourmap.values())