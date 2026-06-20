class Solution:
    def rob(self, nums: List[int]) -> int:

        memo = [-1] * len(nums)
        def dp(i):

            #base case - i reached the last index
            if i >= len(nums):
                return 0
            # base case - if we already solved it
            if memo[i] != -1:
                return memo[i]
            
            # call dp
            memo[i] = max(dp(i+1), nums[i] + dp(i+2))
            return memo[i]

        return dp(0)


    
        