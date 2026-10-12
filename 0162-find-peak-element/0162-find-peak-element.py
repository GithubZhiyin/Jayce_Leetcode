class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 0
        l, r = 0, len(nums) - 1
        nums.append(-float('inf'))
        nums.append(-float('inf'))
        
        while l < r:
            m = l + (r - l) // 2
            if max(nums[m - 1], nums[m + 1]) < nums[m]:
                return m 
            elif nums[m - 1] > nums[m]:
                r = m - 1
            elif nums[m + 1] > nums[m]:
                l = m + 1
        return l 
        

                    