class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0]*n #since the result is in list type 
        for v in bookings:
            res[v[0]-1] += v[2] # take reservation of the seats
            if v[1] < n:
                res[v[1]] -= v[2]
        for i in range(1,n): #use prefix sum
            res[i] += res[i-1]
        return res
