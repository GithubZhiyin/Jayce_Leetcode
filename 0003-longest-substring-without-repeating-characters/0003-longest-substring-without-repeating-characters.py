class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0 
        last = {}
        max_len = 0

        while r < len(s):
            if s[r] in last and l <= last[s[r]]:
                max_len = max(max_len, r - l)
                l = last[s[r]] + 1
            last[s[r]] = r
            r += 1
        
        return max(r - l, max_len)
            
