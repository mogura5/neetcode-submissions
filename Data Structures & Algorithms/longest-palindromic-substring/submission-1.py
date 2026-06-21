class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        if n == 0:
            return ""
        start = 0
        maxLen = 1
        dp = [[False] * n for _ in range(n)]

        # single char
        for i in range(n):
            dp[i][i] = True

        # two chars together
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                start = i
                maxLen = 2

        for length in range(3, n+1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    start, maxLen = i, length
        

        return s[start:start + maxLen]


        