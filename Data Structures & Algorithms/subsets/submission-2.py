class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        stack = []
        def backtrack(i):

            if len(nums) <= i:
                result.append(stack.copy())
                return
            
            stack.append(nums[i])
            backtrack(i + 1)
            stack.pop()
            backtrack(i + 1)
            
        backtrack(0)
        return result