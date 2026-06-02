class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        distance = []
        for x, y in points:
            d = math.sqrt((x)**2 + (y)**2)
            distance.append([d, x, y])
        heapq.heapify(distance)

        res = []
        while k > 0:
            dist, x, y = heapq.heappop(distance)
            res.append([x, y])
            k -= 1
        
        return res
