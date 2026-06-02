class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def backtrack(i, curr, cumSum):
            if cumSum == target:
                result.append(curr.copy())
                return
            if i >= len(nums) or cumSum > target:
                return
            curr.append(nums[i])
            backtrack(i, curr, cumSum + nums[i])
            curr.pop()
            backtrack(i + 1, curr, cumSum)

        backtrack(0, [], 0)
        return result