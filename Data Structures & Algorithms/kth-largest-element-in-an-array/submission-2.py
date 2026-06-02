class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        maxNums = []
        result = []
        for n in nums:
            maxNums.append(n)
        heapq.heapify(maxNums)
        while len(maxNums) > k:
            heapq.heappop(maxNums)
        
        return maxNums[0]

        
        


