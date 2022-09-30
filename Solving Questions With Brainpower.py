class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        points = [x[0] for x in questions]
        mmax = 0
        for i in range(len(questions) -1,-1,-1):
            if i + questions[i][1] + 1 > len(questions) -1:
                mmax = max( points[i], mmax)
            else:
                mmax = max(points[i] + points[i+questions[i][1]+1],mmax)
            points[i] = mmax
        return points[0]
    
