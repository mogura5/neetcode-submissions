class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapNums = []
        for n in nums:
            heapNums.append(-n)

        heapq.heapify(heapNums)

        result = 0
        for i in range(k):
            result = heapq.heappop(heapNums)

        return -result


