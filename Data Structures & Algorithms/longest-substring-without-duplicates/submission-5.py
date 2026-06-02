class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        charMap = {}
        longestS = 0

        while right <= len(s) - 1:

            if s[right] in charMap:
                lastSeen = charMap.get(s[right])
                charMap[s[right]] = right
                left = max(lastSeen + 1, left)
            else:
                charMap[s[right]] = right

            longestS = max(longestS, right - left + 1)
            right = right + 1
        return longestS

