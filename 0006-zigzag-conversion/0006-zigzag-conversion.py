class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        ans = [''] * numRows

        i, direct = 0, 1
        for c in s:
            ans[i] += c
            if i == numRows - 1:
                direct = -1
            elif i == 0:
                direct = 1
            i += direct
        
        return ''.join(ans)





        