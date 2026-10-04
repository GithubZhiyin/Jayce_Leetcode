class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10 ** 9 + 7

        dp_1 = [0 for i in range(n)] #第一个位置和第三个位置相同
        dp_2 = [0 for i in range(n)] #三个位置的颜色都不相同

        dp_1[0] = 6
        dp_2[0] = 6

        for i in range(1, n):
            dp_1[i] = (dp_1[i - 1] * 3 + dp_2[i - 1] * 2) % MOD
            dp_2[i] = (dp_1[i - 1] * 2 + dp_2[i - 1] * 2) % MOD
        
        return (dp_1[-1] + dp_2[-1]) % MOD

        