class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lists = defaultdict(list)
        for i in strs:
            s = sorted(i)
            lists[tuple(s)].append(i)
        
        return list(lists.values())