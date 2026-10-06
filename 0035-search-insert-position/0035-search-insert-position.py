class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if nums[0] >= target:
            return 0
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l + 1) // 2
            if nums[m] == target:
                return m
            if nums[m] <= target:
                l = m
            else:
                r = m - 1
        return l + 1
            