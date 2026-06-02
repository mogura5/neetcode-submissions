class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs is None:
            return strs
        res = defaultdict(list)

        for s in strs:
            sortS = ''.join(sorted(s))
            res[sortS].append(s)
        return list(res.values())
        
