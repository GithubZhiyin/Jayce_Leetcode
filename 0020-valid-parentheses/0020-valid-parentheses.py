class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'(':')', '[':']', '{':'}'} 
        for x in s:
            if x in pairs:
                stack.append(x)
            else:
                if len(stack) > 0  and pairs[stack[-1]] == x:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0

