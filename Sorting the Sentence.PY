class Solution:
    def sortSentence(self, s: str) -> str:
        temp = s.split()
        temp_out=[0 for i in temp]
        for i in temp:
            j = int(i[-1])
            temp_out[j-1] = i[:len(i)-1]
        return ' '.join(temp_out)
            
