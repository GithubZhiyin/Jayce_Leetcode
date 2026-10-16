class Solution:
    def intToRoman(self, num: int) -> str:
        info = [['I', 'V'], ['X', 'L'], ['C', 'D'], ['M'] ]

        ans = ''
        i = 0 
 
        while num > 0:
            curr = num % 10
            if curr == 4:
                ans += info[i][1] + info[i][0]
            elif curr == 9:
                ans += info[i + 1][0] + info[i][0]
            elif curr < 5:
                ans += curr * info[i][0]
            elif curr >= 5:
                ans += (curr - 5) * info[i][0] + info[i][1]
            num //= 10 
            i += 1
        
        return ans[::-1]


