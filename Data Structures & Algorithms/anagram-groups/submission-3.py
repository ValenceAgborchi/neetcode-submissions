class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ourhashmap = defaultdict(list)

        for i in strs:
            sortedstring = ''.join(sorted(i))
            ourhashmap[sortedstring].append(i)

        return list(ourhashmap.values())



            