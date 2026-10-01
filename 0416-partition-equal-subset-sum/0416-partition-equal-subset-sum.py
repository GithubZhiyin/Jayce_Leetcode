class Solution:
    def canPartition(self, nums: list[int]) -> bool:

        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        n = len(nums)
        memo = {}

        def dfs(i, remain):
            if remain == 0:
                return True
            if i == n or remain < 0:
                return False
            if (i, remain) in memo:
                return memo[(i, remain)]

            res = dfs(i + 1, remain - nums[i]) or dfs(i + 1, remain)
            memo[(i, remain)] = res
            return res

        return dfs(0, target)

            

            





        