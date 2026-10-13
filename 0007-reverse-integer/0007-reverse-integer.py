class Solution:
    def reverse(self, x: int) -> int:

        ans = 0 
        if x >= 0:
            while x:
                add = x % 10
                if ans < (2 ** 31 - 1 - add) / 10:
                    ans = ans * 10 + add
                    x = x // 10
                else:
                    return 0 
            return ans 
        if x < 0:
            x = -x
            while x:
                add = x % 10
                if ans < (2 ** 31 - add) / 10:
                    ans = ans * 10 + add
                    x = x // 10
                else:
                    return 0 
            return -ans 



            
        