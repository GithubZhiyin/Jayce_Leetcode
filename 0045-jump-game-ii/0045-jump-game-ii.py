class Solution:
    def jump(self, nums: list[int]) -> int:

        n = len(nums)
        if n == 1:
            return 0

        i = 0
        cur_end = 0     
        b = 0               
        jump = 0

        while i <= cur_end:              
            b = max(b, i + nums[i])     
            if cur_end >= n - 1:       
                break
            if i == cur_end:           
                jump += 1
                cur_end = b       
            i += 1

        return jump
                

            
