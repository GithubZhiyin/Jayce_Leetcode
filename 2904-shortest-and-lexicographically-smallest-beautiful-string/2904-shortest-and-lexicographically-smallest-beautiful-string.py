class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ans = '1' * 101
        count_1 = 0 
        list_1 = []
        last_1 = 0

        for i, s_i in enumerate(s):
            if count_1 < k and s_i == '1':
                count_1 += 1
                list_1.append(i)
                
            if count_1 == k:
                theshy = s[list_1[last_1]: i + 1]
                if int(theshy) < int(ans):
                    ans = theshy
                last_1 += 1
                count_1 -= 1

        return ans if last_1 else ""
            


                


