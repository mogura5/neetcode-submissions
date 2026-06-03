class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums = sorted(nums)

        def backtrack(i, subset):

            if i == len(nums):
                # copy is critical because subset is mutated across each level, so you need a snapshot
                output.append(subset.copy())
                return
            #include
            subset.append(nums[i])
            backtrack(i + 1, subset)

            #skip / not include
            subset.pop()

            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(i + 1, subset)

        backtrack(0, [])
        
        return output