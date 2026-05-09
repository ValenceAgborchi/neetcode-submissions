class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ourmap = defaultdict(list)
        for i in strs:
            count = [0] * 26
            for k in i:
                count[ord(k) - ord('a')] += 1
            ourmap[tuple(count)].append(i)
        return list(ourmap.values())