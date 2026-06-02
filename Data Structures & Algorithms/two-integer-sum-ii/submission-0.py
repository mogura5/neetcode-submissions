class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            addSum = numbers[left] + numbers[right]

            if addSum == target:
                return [left + 1, right + 1]
            
            if addSum < target:
                left += 1
            if addSum > target:
                right -= 1
        return []