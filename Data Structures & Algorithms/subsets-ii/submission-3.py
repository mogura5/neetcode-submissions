class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        output = []
        nums = sorted(nums)

        def backtrack(i, subset):
            # base case
            if i == len(nums):
                output.append(subset.copy())
                return
            
            #include
            subset.append(nums[i])
            backtrack(i+1, subset)

            #don't include
            subset.pop()
            #don't include duplicates
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(i+1, subset)
        backtrack(0, [])
        return output