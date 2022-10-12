class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        temp1 = [0] * 1001 #since   0 <= fromi < toi <= 1000
        trips.sort(key=lambda x:x[1]) #sort the trips by starting location
        for trip in trips:
            temp1[trip[1]] += trip[0]
            temp1[trip[2]] -= trip[0]
        
        i = 0
        while i < len(temp1) and capacity >= 0:
            capacity -= temp1[i]
            i += 1
        return True if capacity >= 0 else False
          
