# the first code tgave me run time error, and the second worket well

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        output = []
        i = 0
        while i < len(intervals)-1:
            temp1 = intervals[i]
            temp2 = intervals[i+1]

            if temp1[1] >= temp2[0]:
                temp = [min(temp1[0], temp2[0]), max(temp1[1], temp2[1])]
                output.append(temp)
            else:
                output.append(temp1)
                output.append(temp2)
            i +=2
        return output
      
 #####################################################
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        output = []
        
        intervals.sort()
        for llist in intervals:
            if len(output) == 0 or output[-1][1] < llist[0]:
                output.append(llist)
            else:
                output[-1][1] = max(output[-1][1], llist[1])
                
        return output
            
