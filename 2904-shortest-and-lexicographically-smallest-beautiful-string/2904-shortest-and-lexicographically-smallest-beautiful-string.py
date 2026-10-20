class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ans = ""
        list_1 = [] 
        left = 0  
        
        for i, char in enumerate(s):
            if char == '1':
                list_1.append(i)
            
            if len(list_1) - left == k:
                sub = s[list_1[left] : i + 1]
                if ans == "" or len(sub) < len(ans) or (len(sub) == len(ans) and sub < ans):
                    ans = sub
                left += 1
                
        return ans
            


                


