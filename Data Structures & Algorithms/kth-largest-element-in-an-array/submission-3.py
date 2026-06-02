class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapNums = []
        for n in nums:
            heapNums.append(-n)

        heapq.heapify(heapNums)

        result = []
        for i in range(k):
            result.append(heapq.heappop(heapNums))

        return -(result[k - 1])


