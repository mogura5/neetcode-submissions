class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)      # +1 because top is past last index

        # base cases
        dp[0] = 0
        dp[1] = 0

        # fill bottom up
        for i in range(2, n + 1):
            dp[i] = min(
                dp[i-1] + cost[i-1],   # came from one step below
                dp[i-2] + cost[i-2]    # came from two steps below
            )

        return dp[n]