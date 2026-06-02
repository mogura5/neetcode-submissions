class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        sortedStones = []
        for s in stones:
            sortedStones.append(-s)

        heapq.heapify(sortedStones)

        while len(sortedStones) > 1:

            first = heapq.heappop(sortedStones)
            second = heapq.heappop(sortedStones)

            newFirst = first - second

            heapq.heappush(sortedStones, newFirst)
        return -(sortedStones[0])