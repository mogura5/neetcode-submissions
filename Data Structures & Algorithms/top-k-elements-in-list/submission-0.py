class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        result = []
        dummy = []

        for num in nums:

            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
            
        for key in hashmap:
            dummy.append([hashmap[key], key])

        dummy.sort()
        dummy.reverse()

        for i in range(k):
            result.append(dummy[i][1])
        return result

        
