class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] >= target:
                r = m 
            else:
                l = m + 1
        res_1 = r

        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l + 1) // 2
            if nums[m] <= target:
                l = m
            else:
                r = m - 1
        res_2 = l

        if len(nums) == 0:
            return [-1, -1]
        if nums[res_1] == nums[res_2] == target:
            return [res_1, res_2]
        else:
            return [-1, -1]

        



