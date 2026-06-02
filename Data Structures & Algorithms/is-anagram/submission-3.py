class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}

        for letter in s:

            if letter in hashmap:
                hashmap[letter] += 1
            else:
                hashmap[letter] = 1
            
        for letter2 in t:

            if letter2 in hashmap:
                hashmap[letter2] -= 1
            else:
                return False 
        
        for val in hashmap.values():
            if val == 0:
                continue
            else:
                return False
        return True
        

