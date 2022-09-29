#in the first attempt I tried this but it gave me RUNTIME ERROR , do I changed my mind 
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        templist = []
        tempdic = {}

        for llist in points:
            distance = (llist[0] * llist[0]) + (llist[1] * llist[1])
            templist.append(distance)
            tempdic[str(llist)] = distance

        templist.sort()
        output = []
        i = 0
        while i < k:
            val = templist[i]
            temp2 = []
            for key, value in tempdic.items():
                if val == value:

                    if key[1] == '-':
                        temp2.append(-1*int(key[2]))
                    elif key[1] != '-':
                        temp2.append(int(key[1]))
                    if key[-3] == '-':
                        temp2.append(-1 * int(key[-2]))
                    elif key[-3] != '-':
                        temp2.append(int(key[-2]))
            output.append(temp2)
            i +=1
        return output
             
 #this worked well.
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x,y in points:
            heapq.heappush(heap,((math.sqrt(x**2 + y**2)),[x,y]))
            
        output = []
        i = 1
        while heap and i <= k:
            h= heapq.heappop(heap)
            output.append(h[1])
            i +=1
        return output
        
