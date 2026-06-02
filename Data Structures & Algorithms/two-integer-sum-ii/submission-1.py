class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left <= right:
            addedSum = numbers[left] + numbers[right]

            if addedSum == target:
                return [left + 1, right + 1]
            
            if addedSum < target:
                left = left + 1
                
            elif addedSum > target:
                right = right - 1
                 
        return []