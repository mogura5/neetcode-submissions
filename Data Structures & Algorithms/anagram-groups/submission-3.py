class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dictionary = {}
        result = []

        for s in strs:
            key = ''.join(sorted(s))

            if key in dictionary:
                dictionary[key].append(s)
            else:
                dictionary[key] = [s]

        for val in dictionary.values():
            result.append(val)
            


        print(dictionary)
        return result
        

        

        
        
        
