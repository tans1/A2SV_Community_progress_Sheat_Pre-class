class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        temdic={}
        prefix = counter =0

        for i in nums:
            
            prefix += i
            if prefix == k:   
                counter += 1
            if prefix-k in temdic: 
                counter += temdic[prefix-k]
            
            if prefix in temdic:
                temdic[prefix]+=1
            else:
                temdic[prefix]=1

        return counter
