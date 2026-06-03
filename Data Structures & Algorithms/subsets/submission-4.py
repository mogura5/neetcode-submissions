class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [] # final list of all subsets
        subset = [] # current subset being built

        def dfs(i):
            if i == len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)

        dfs(0) # 0 is the starting index
        return res