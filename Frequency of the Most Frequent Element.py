class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        maxx = summ = i = j = 0
        while j < len(nums):
            summ += nums[j]
            while (nums[j]*(j-i+1) - summ > k):
                summ -= nums[i]
                i += 1
            maxx = max(maxx, j - i + 1);
            j += 1
        return maxx
