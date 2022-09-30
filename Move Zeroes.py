class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        for nonZero in range(len(nums)):
            if nums[nonZero] != 0:
                nums[zero], nums[nonZero] = nums[nonZero], nums[zero]
                zero += 1
        
        #we can also use this , but it doesnt maintain the order
        i = 0 #zero finder
        j = len(nums)-1 #non-zero finder

        while i < j:
            if nums[i] != 0:
                i +=1
            if nums[j] == 0:
                j -=1
            if nums[i] ==0 and nums[j] !=0:
                nums[i] , nums[j] = nums[j], nums[i]
                i +=1
                j -=1
