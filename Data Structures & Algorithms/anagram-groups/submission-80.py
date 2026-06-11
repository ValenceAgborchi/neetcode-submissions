class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)

        for i in strs:
            sorteds = ''.join(sorted(i))
            output[sorteds].append(i)

        return list(output.values())