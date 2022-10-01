class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        f = firstLen 
        s = secondLen 
        if len(nums) < s + f: return 0
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        res, maxf, maxs = nums[f + s - 1], nums[f - 1], nums[s - 1]
        for i in range(f + s, len(nums)):
            maxf = max(maxf, nums[i - s] - nums[i - s - f])
            maxs = max(maxs, nums[i - f] - nums[i - f - s])
            res = max(res, maxf + nums[i] - nums[i - s], maxs + nums[i] - nums[i - f])
        return res
