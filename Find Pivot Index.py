class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
      
    ## This worked for 598 test cases, UNFORTUNATELY it failed at 599
        pre1 = []
        pre1.append(nums[0])
        for i in range(1,len(nums)):
            pre1.append(pre1[-1]+nums[i])
        pre2 = []
        a = nums[::-1]
        pre2.append(a[0])
        for i in range(1,len(a)):
            pre2.append(pre2[-1]+a[i])
        pre2 = pre2[::-1]
        
        i = 0
        while i < len(pre1)-2:
            if pre1[i] == pre2[i+2]:
                return i+1
            i +=1

        if pre1[0] == pre2[0] and pre2[1] == 0:
            return 0
        else:
            return -1

      ## However this worked well
        
        left = 0
        right = sum(nums)
        for i in range(len(nums)):
            right -= nums[i]
            if left == right:
                return i
            left += nums[i]
        return -1
        
