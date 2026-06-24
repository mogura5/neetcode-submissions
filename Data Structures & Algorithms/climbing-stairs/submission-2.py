class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1] * n

        def dp(i):

            # base case
            if i > n:
                return 0
            if i == n:
                return 1
            if memo[i] != -1:
                return memo[i]
            
            memo[i] = dp(i + 1) + dp(i + 2)
            return memo[i]

        return dp(0)


        