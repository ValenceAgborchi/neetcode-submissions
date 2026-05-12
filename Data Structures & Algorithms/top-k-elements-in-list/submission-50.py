class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ourmap = defaultdict(list)

        for i in nums:
            ourmap[i] = 1 + ourmap.get(i, 0)
        
        sortlist = []
        for num, count in ourmap.items():
            sortlist.append([count, num])
        sortlist.sort()

        result = []
        while len(result) < k:
            result.append(sortlist.pop()[1])
        return result
 
        



        
        

