class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ourmap = defaultdict(list)
        for i in strs:
            sort = ''.join(sorted(i))
            ourmap[sort].append(i)
        
        return list(ourmap.values())
       