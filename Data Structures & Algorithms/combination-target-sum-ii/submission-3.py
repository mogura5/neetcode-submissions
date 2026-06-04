class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        candidates = sorted(candidates)
        def backtrack(i, sumVal, subset):

            # base case
            if sumVal == target:
                output.append(subset.copy())
                return
            if sumVal > target or i == len(candidates):
                return
            
            # include
            subset.append(candidates[i])
            backtrack(i + 1, sumVal + candidates[i], subset)
            # not include
            subset.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i + 1, sumVal, subset)

        backtrack(0, 0, [])
        return output