class Solution:
    def decodeString(self, s: str) -> str:
        stack1 = [] #for the letters
        stack2 = [] #for the number of repeatition
        counter = 0
        output = ''
        
        for i in range(len(s)):
            if s[i] not in '0123456789' and s[i] != '[' and s[i] != ']':
                stack2.append(s[i])
            if s[i] in '0123456789':
                counter = counter * 10 + int(s[i])
            elif s[i] == '[':
                stack1.append([counter,stack2])
                stack2 = []
                counter = 0
            elif s[i] == ']':
                top = stack1.pop()
                stack2 = top[1] + top[0]*stack2

        return ''.join(stack2)
