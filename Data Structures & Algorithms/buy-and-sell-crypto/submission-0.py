class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        maxProf = 0

        if len(prices) == 1:
            return 0
        
        while 0 <= right and right <= len(prices) - 1:
            
            if prices[right] > prices[left]:
                maxProf = max(maxProf, prices[right] - prices[left])

            if prices[right] < prices[left]:
                left = right

            right += 1
        return maxProf



        