class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = {}
        for i in nums:
            output[i] = 1 + output.get(i, 0)
        
        arr = []
        for i, cnt in output.items():
            arr.append([cnt, i])
        arr.sort()

        answer = []
        while len(answer) < k:
            answer.append(arr.pop()[1])

        return answer

       