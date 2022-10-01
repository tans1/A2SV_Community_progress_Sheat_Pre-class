class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        tempnum = [int(i) for i in nums]
        tempnum.sort()
        num = tempnum[::-1]
        if k > len(num):
            return None
        return str(num[k-1])
# WE CAN ALSO USE HEAP, WHICH IS MORE EFFICIENT
