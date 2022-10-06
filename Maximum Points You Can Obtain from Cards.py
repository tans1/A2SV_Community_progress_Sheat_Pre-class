class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        res = 0
        n = len(cardPoints)
        total = sum(cardPoints)
        window = sum(cardPoints[:n-(k+1)])
        if k == n: return total
        
        for i in range(n-(k+1),n):
            window += cardPoints[i]
            res = max(res, total - window)
            window -= cardPoints[i -(n-k-1)]
        return res
