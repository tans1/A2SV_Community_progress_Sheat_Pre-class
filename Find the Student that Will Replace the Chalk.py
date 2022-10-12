class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        i , n = 0, len(chalk)
        while chalk[i % n] <= k:
            k -= chalk[i % n]
            i += 1
        return i % n
    
        i = summ = 0
        n = len(chalk)
        while summ < k:
            summ += chalk[i%n]
            i += 1
        if summ >= k:
            return i%n
# both the above works , but the time limit is exceeded, but
        summ = k % sum(chalk)  #this will pass the time limit exceed
        for i in range(len(chalk)):
            if summ - chalk[i] < 0:
                return i
            summ -= chalk[i]
        
