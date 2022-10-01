class Solution:
    def isValid(self, s: str) -> bool:
        llist = [s[i] for i in range(len(s))]  
        stack = []

        dic = {
            ']' : '[',
            '}' : '{',
            ')' : '('
            }

        for i in llist:
            if i in ['[','(','{']:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                else:
                    top = stack.pop()
                    if top != dic[i]:
                        return False
        if len(stack) == 0:
            return True
        else:
            return False
