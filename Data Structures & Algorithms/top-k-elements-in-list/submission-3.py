class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dummy = []
        hashmap = {}
        result = []

        for n in nums:
            
            if n in hashmap:
                hashmap[n] += 1
            else:
                hashmap[n] = 1
        
        for i in hashmap:
            dummy.append([-hashmap[i], i])
        
        dummy.sort()

        for i in range(len(dummy[:k])):
            result.append(dummy[i][1])

        return result