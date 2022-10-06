class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if 0 not in nums: return len(nums) - 1
        zerocounter = 1
        left = 0
        for j in range(len(nums)):
            if nums[j] == 0:
                zerocounter -= 1
            if zerocounter < 0:
                if nums[left] == 0:
                    zerocounter += 1
                left += 1
        return j - left
