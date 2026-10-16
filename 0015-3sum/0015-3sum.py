class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = []
        nums.sort()
        n = len(nums)
        l = 0
        while l < n - 2:
            if nums[l] > 0:            
                break
            if l > 0 and nums[l] == nums[l - 1]:
                l += 1               
                continue
            m, r = l + 1, n - 1
            target = -nums[l]
            while m < r:
                s = nums[m] + nums[r]
                if s == target:
                    ans.append([nums[l], nums[m], nums[r]])
                    m += 1
                    while m < r and nums[m] == nums[m - 1]:  
                        m += 1
                    r -= 1
                    while m < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif s < target:
                    m += 1
                else:
                    r -= 1
            l += 1
        return ans

            

        