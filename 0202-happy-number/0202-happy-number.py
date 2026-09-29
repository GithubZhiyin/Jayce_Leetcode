class Solution:
    def isHappy(self, n: int) -> bool:
        ans_dict = {}
        num = n
        while num not in ans_dict:
            sum_d = 0
            ans_dict[num] = None
            while num > 0:
                sum_d += (num % 10) ** 2
                num //= 10 
            num = sum_d
            if num == 1:
                return True
        return False
                

