class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        hashmap = {}
        maxf = 0
        res = 0
        for right in range(len(s)):
            if s[right] in hashmap:
                hashmap[s[right]] += 1
            else:
                hashmap[s[right]] = 1

            maxf = max(maxf, hashmap[s[right]])

            while (right - left + 1) - maxf > k:
                hashmap[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res
            

            