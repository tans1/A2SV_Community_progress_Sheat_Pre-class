class Solution:
    def calculate(self, s: str) -> int:
        stack ,operator, val = [],'+' , 0
        for i in range(len(s)):
            if s[i].isdigit(): 
                val = 10*val + int(s[i])      
                
            if s[i] in "+-*/" or i == len(s) - 1: #
                if   operator == "+": 
                    stack.append(val)
                elif operator == "-": 
                    stack.append(-val)
                elif operator == "*": 
                    stack.append(stack.pop() * val)
                elif operator == "/": 
                    stack.append(int(stack.pop()/val))
                operator = s[i]
                val = 0
        return sum(stack)
