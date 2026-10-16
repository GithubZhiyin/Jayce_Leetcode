class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest_sum = nums[0] + nums[1] + nums[2] 
        
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # 剪枝1：以 nums[i] 能组成的最小和
            min_sum = nums[i] + nums[i + 1] + nums[i + 2]
            if min_sum > target:
                if abs(min_sum - target) < abs(closest_sum - target):
                    closest_sum = min_sum
                break  # 后续 i 只会更大
            
            # 剪枝2：以 nums[i] 能组成的最大和
            max_sum = nums[i] + nums[n - 2] + nums[n - 1]
            if max_sum < target:
                if abs(max_sum - target) < abs(closest_sum - target):
                    closest_sum = max_sum
                continue
            
            p1, p2 = i + 1, n - 1
            while p1 < p2:
                s = nums[i] + nums[p1] + nums[p2]
                if s == target:
                    return target
                if abs(s - target) < abs(closest_sum - target):
                    closest_sum = s
                if s > target:
                    p2 -= 1
                    while p1 < p2 and nums[p2] == nums[p2 + 1]:
                        p2 -= 1
                else:
                    p1 += 1
                    while p1 < p2 and nums[p1] == nums[p1 - 1]:
                        p1 += 1
        
        return closest_sum