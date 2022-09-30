class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        result = oddcounter = 0
        prefix = {}
        prefix[0] = 1
        for i in range(len(nums)):
            if nums[i] % 2 != 0:
                oddcounter += 1
            if oddcounter in prefix:
                prefix[oddcounter] += 1
            else: 
                prefix[oddcounter] = 1
        for y in prefix:
            if y - k in prefix:
                result += prefix[y] *prefix[y - k]
        return result
        
        
 ## This one also works for most of the test cases , but failed for some, but with a little modification it canbe used
        tempdic = {}
        prefix = []
        counter = 0
        for i in nums:
            if i == k:
                counter += 1
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] =1
        tempdic[0] = 1
        for i in nums:
            if i == k:
                counter +=1
            if len(prefix) == 0:
                prefix.append(i)
                tempdic[i] = 1
            else:
                prefix.append(prefix[-1] + i)
                if prefix[-1] in tempdic:
                    tempdic[prefix[-1]] +=1
                else:
                    tempdic[prefix[-1]] = 1
        for y in prefix:
            if y - k in tempdic:
                counter += tempdic[y-k]
        return counter
        
        
        
        
