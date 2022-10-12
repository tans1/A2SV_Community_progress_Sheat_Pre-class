class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a','e','i','u','o','A','E','I','O','U']
        count = 0
        for i in range(k):
            count += s[i] in vowels
        res = count
        for i in range(k, len(s)):
            count += s[i] in vowels
            count -= s[i - k] in vowels
            res = max(res, count)
        return res
    ## Unfortunately this failed at 99/106 testcase )::
    
        i = maxx = 0
        j = k
        while j <= len(s):
            window = s[i:j]
            count = 0
            a = 0
            while a < len(window):  #iterate inside the window with a index
                if window[a] in vowels:
                    count += 1
                a += 1
            maxx = max(maxx ,count)
            i += 1 #shift the window to left
            j += 1
        return maxx
                
                
