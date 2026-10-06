class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m - 1] == nums[m]:
                if (m - 1 - l) % 2 == 0:
                    l = m + 1
                else:
                    r = m - 2
            elif nums[m + 1] == nums[m]:
                if (m - l) % 2 == 0:
                    l = m + 2
                else:
                    r = m - 1
            else:
                return nums[m]
        return nums[l]



            
        