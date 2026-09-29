class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(n):
            ans = 0
            while n > 0:
                n, d = divmod(n, 10)
                ans += d * d
            return ans
        
        slow, fast = n, get_next(n)
        while slow != fast and fast != 1:
            slow = get_next(slow)
            fast = get_next(get_next(fast))
        
        return fast == 1


                

