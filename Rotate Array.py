class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(nums, i, j):
            while (i < j):
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
            return nums
        if len(nums) > 1:
            k = k % len(nums)
            reverse(nums, 0, len(nums) - 1)  # rotate entire array
            reverse(nums, 0, k - 1)          # rotate array upto k elements
            reverse(nums, k, len(nums) - 1)  # rotate array from k to end of array
    
############################################################        
#this also works, but since inserting an element at a position requires to move the elements after it, the time complexity will be higher
        i = 0
        while i < k:
            a = nums.pop()
            nums.insert(0,a)
            i +=1
    

        
        
        
