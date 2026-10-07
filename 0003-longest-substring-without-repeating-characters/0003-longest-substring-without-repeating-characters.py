class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0 
        hash_table = {}

        max_len = 0
        while r < len(s):
            if s[r] not in hash_table:
                hash_table[s[r]] = r
                r += 1
            else:
                max_len = max(r - l, max_len)
                l, r = hash_table[s[r]] + 1, hash_table[s[r]] + 1
                hash_table = {}
        return max(r - l, max_len)  