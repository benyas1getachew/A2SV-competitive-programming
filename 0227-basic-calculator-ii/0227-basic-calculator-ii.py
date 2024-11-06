class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        operator = '+'
        
        for i, char in enumerate(s):
            if char.isdigit():
                num = num * 10 + int(char)
            if char in "+-*/" or i == len(s) - 1:
                if operator == '+':
                    stack.append(num)
                elif operator == '-':
                    stack.append(-num)
                elif operator == '*':
                    stack[-1] *= num
                elif operator == '/':
                    stack[-1] = int(stack[-1] / num)
                
                operator = char
                num = 0

        return sum(stack)