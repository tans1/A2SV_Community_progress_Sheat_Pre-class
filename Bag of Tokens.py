class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        if len(tokens) == 0 or power < tokens[0] : return 0
        stack = []
        left = 0
        right = len(tokens)-1
        score = 0
        while left <= right:
            if power >= tokens[left] :
                score += 1
                power -= tokens[left]
                left += 1
            elif power < tokens[left] and score >= 1:
                score -= 1
                power += tokens[right]
                right -= 1
            stack.append(score)
        return max(stack)
            
