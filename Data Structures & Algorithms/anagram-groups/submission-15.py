class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ourmap = defaultdict(list)
        for i in strs:
            if i not in ourmap:
                ourmap[tuple(sorted(i))].append(i)
        return list(ourmap.values())

