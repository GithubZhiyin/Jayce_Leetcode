class Solution:
    def findMin(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 1
        
        while l < r :
            m = (l + r) >> 1
            if nums[l] < nums[r]:
                return nums[l]
            else:
                if nums[m] > nums[r]:
                    l = m + 1
                elif nums[m] < nums[r]:
                    r = m 

        return nums[l]
        