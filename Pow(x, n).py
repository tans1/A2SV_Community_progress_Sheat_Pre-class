class Solution:
    def myPow(self, x: float, n: int) -> float:
        N = n
        if n >= 0:
            temp1 = n
        else:
            temp1 = n * -1

        if temp1 == 0:
            return 1
          
        elif x == 0:
            return 0
          
        temp = self.myPow(x,temp1 // 2)
        temp *= temp
        output = temp*x if n%2 else temp
        
        return output if N>=0 else 1/output
