class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = 2 * len(nums)
        n = len(nums)
        result = [0] * length

        for i in range(n):

            result[i] = nums[i]
            result[i + n] = nums[i]
        return result
