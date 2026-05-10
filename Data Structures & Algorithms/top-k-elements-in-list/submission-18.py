class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ourmap = defaultdict(list)

        for i in nums:
            ourmap[i] = ourmap.get(i, 0) + 1
        
        ourlist = []

        for i, num in ourmap.items():
            ourlist.append([num, i])
        ourlist.sort()

        result = []

        while len(result) < k:
            result.append(ourlist.pop()[1])
        
        return result

     

 