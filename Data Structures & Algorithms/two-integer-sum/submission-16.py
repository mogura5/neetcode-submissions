class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, num in enumerate(nums):
    
            diff = target - nums[i]

            if diff in hashmap:

                return [min(i, hashmap[diff]),
                max(i, hashmap[diff])]
            
            hashmap[num] = i
