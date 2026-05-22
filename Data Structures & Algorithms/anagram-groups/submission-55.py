class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ourmap = defaultdict(list)
        for i in strs:
            sorteds = sorted(i)
            ourmap[tuple(sorteds)].append(i)

        return list(ourmap.values())


      