class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans, suffix_prod = [1]*len(nums), 1
        for i in range(1,len(nums)):  #first assign prefixes for all the i in nums
            ans[i] = ans[i-1] * nums[i-1]
        for i in range( len(nums) -1,-1,-1):  #then multiply with its suffixes
            ans[i] *= suffix_prod
            suffix_prod *= nums[i]
        return ans
