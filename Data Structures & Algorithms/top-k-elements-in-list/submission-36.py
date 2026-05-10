class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ourmap = {}
        for i in nums:
            ourmap[i] = ourmap.get(i, 0) + 1
        
        ourlist = []
        for num, count in ourmap.items():
            ourlist.append([count, num])
        ourlist.sort()

        result = []
        while len(result) < k:
            result.append(ourlist.pop()[1])
        
        return result

  
        



        
        

