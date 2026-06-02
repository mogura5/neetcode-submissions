class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0 
        right = 1
        maxProf = 0

        while right <= len(prices) - 1:

            if prices[left] < prices[right]:
                maxProf = max(maxProf, prices[right] - prices[left])
            
            elif prices[right] < prices[left]:
                left = right
            
            right += 1
        return maxProf