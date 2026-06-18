class Solution:
    def rob(self, nums: List[int]) -> int:

        # use memo to store each maximum amount of money from house i
        memo = [-1] * len(nums)

        def dp(i):
            # base case
            if i >= len(nums):
                return 0
            if memo[i] != -1:
                return memo[i]

            # at each step, we either decide to rob it or skip it
            memo[i] = max(dp(i + 1), nums[i] + dp(i + 2))
            return memo[i]

        return dp(0)


        