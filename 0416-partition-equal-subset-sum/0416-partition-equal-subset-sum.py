class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        target = sum(nums)
        if target % 2 != 0:
            return False
        target //= 2

        memo = {}

        def dfs(i, remain):
            if (i, remain) in memo:
                return memo[(i, remain)]
            
            if i >= len(nums) or remain < 0:
                return False
            if remain == 0:
                return True
            
            res = dfs(i + 1 , remain) or dfs(i + 1, remain - nums[i])
            memo[(i, remain)] = res
            return res
        
        return dfs(0, target)
            



        
