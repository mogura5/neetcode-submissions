class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1

        result = []
        for i, num in enumerate(nums):
            result.append([num, i])

        result.sort()
        
        while left < right:

            addedSum = result[left][0] + result[right][0]

            if addedSum == target:
                return [min(result[left][1],result[right][1]),
                        max(result[left][1],result[right][1])]
            
            if addedSum < target:
                left += 1
            else:
                right -= 1
