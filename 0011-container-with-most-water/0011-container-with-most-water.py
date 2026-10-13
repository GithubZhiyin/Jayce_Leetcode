class Solution:
    def maxArea(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        ans = -1
        while l < r:
            curr_ = (r - l) * min(height[r], height[l])
            ans = max(curr_, ans)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return ans 
