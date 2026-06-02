class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        topK = {}
        for n in nums:
            if n in topK:
                topK[n] += 1
            else:
                topK[n] = 1
        heap = []
        for item in topK:
            heapq.heappush(heap, (topK[item], item))

            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for item in range(k):
            res.append(heapq.heappop(heap)[1])
        return res