class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.output = []
        self.backtrack([], nums, [False]*len(nums))
        return self.output

    def backtrack(self, subset, nums, pick):

        # base case
        if len(subset) == len(nums):
            self.output.append(subset.copy())
            return 

        # loop
        for i in range(len(nums)):

            if not pick[i]:
                subset.append(nums[i])
                pick[i] = True
                self.backtrack(subset, nums, pick)

                #backtrack
                subset.pop()
                pick[i] = False    