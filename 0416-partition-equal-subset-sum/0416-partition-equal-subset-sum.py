class Solution:
    def canPartition(self, nums: list[int]) -> bool:

        num_sum = sum(nums)
        if num_sum % 2 != 0:
            return False
        target = num_sum // 2

        memo = {}

        def dfs(i, target):
            if (i, target) in memo:
                return memo[(i, target)]

            if i >= len(nums) or target < 0:
                return False
            if target == 0:
                return True
            
            res = dfs(i + 1, target - nums[i]) or dfs(i + 1, target)
            memo[(i, target)] = res

            return res
        
        return dfs(0, target)