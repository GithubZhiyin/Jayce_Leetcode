class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        def match(x, y):
            return (x == '(' and y == ')') or (x == '{' and y == '}') or (x == '[' and y == ']') 

        for x in s:
            if x in ['(', '{', '[']:
                stack.append(x)
            else:
                if len(stack) == 0:
                    return False
                if match(stack[-1], x):
                    stack.pop()
                else:
                    return False

        return len(stack) == 0
        