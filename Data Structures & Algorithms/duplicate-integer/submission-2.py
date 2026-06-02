class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicateHash = {}

        for n in nums:

            if n in duplicateHash:
                return True
            else:
                duplicateHash[n] = 1
        
        return False
