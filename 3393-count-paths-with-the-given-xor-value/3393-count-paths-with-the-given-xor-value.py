class Solution:
    def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:

        MOD = 10 ** 9 + 7
        m, n = len(grid), len(grid[0])
        dp = [[[0] * 16 for _ in range(n)] for _ in range(m)]
        dp[0][0][grid[0][0]] = 1

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                a = grid[i][j]                     # ✅ 修正
                for v in range(16):
                    prev = v ^ a
                    count = 0
                    if i > 0:
                        count += dp[i - 1][j][prev]
                    if j > 0:
                        count += dp[i][j - 1][prev]
                    dp[i][j][v] = count % MOD      # ✅ 修正

        return dp[m - 1][n - 1][k]