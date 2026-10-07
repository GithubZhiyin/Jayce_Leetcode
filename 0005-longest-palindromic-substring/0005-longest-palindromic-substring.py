class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False] * len(s) for _ in range(len(s))]
        for i in range(len(dp)):
            dp[i][0] = True
        for i in range(len(dp) - 1):
            dp[i][1] = s[i] == s[i + 1] 
        
        for j in range(2, len(dp)):
            for i in range(0, len(dp) - j):
                dp[i][j] = dp[i + 1][j - 2] and s[i] == s[i + j]
        
        for j in range(len(dp) - 1, -1, -1):
            for i in range(0, len(dp) - j):
                if dp[i][j]:
                    return s[i:i + j + 1]
        
        
        