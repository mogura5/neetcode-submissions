class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent = {}
        for n in nums:

            if n in frequent:
                frequent[n] += 1
            else:
                frequent[n] = 1
        
        heap = []
        for num in frequent:
            heapq.heappush(heap, (frequent[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        print(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res