class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        stack = []
        i = 0
        while i < len(l):
            temp = nums[l[i]:r[i]+1]
            check_result = self.check(temp)
            stack.append(check_result)
            i += 1
        return stack
    def check(self,arr):
        arr.sort()
        d = arr[1] - arr[0]
        for i in range(1,len(arr)-1):
            if arr[i+1] - arr[i] != d:
                return False
        return True
