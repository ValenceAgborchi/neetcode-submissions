from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Iterate through list and count instances of each unique value in hashmap
        mostfreq = {}
        for i in nums:
            mostfreq[i] = 1 + mostfreq.get(i, 0)

        # Iterate through key value pairs in hashmap, appending to new list in value-key format to sort (sorting impacts first array value)
        arr = []
        for num, cnt in mostfreq.items():
            arr.append([cnt, num])
        arr.sort()

        #While result length is less than k (want k values returned), append from arr with arr.pop[1] to extract second value in each array (num)
        result = []

        while len(result) < k:
            result.append(arr.pop()[1])
        
        return result


 