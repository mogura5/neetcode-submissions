class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        def backtrack(i, sumVal, subset):

            if sumVal > target or i == len(nums):
                return
            if sumVal == target:
                output.append(subset.copy())
                return

            # include
            subset.append(nums[i])
            backtrack(i, sumVal + nums[i], subset)

            # not include
            subset.pop()
            backtrack(i+1, sumVal, subset)
        
        backtrack(0, 0, [])
        return output