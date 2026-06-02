class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        stack = []

        def dfs(i):

            if i >= len(nums):
                result.append(stack.copy())
                return

            stack.append(nums[i])
            dfs(i + 1)
            stack.pop()
            dfs(i + 1)

        dfs(0)

        return result