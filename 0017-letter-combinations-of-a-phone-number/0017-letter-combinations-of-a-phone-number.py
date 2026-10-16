class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        map_ = {
            2:'abc', 
            3:'def', 
            4:'ghi', 
            5:'jkl', 
            6:'mno', 
            7:'pqrs', 
            8:'tuv', 
            9:'wxyz'
        }
        ans = []
        def backtrace(i, curr):
            if i >= len(digits):
                ans.append(curr)
                return 
            
            for s in map_[int(digits[i])]:
                curr += s
                backtrace(i + 1, curr)
                curr = curr[:-1]
        backtrace(0, '')
        return ans 