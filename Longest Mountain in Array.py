class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        i = maxx =0
        while i < len(arr):
            while i < len(arr)-1 and arr[i] >= arr[i+1]:
                i += 1
            if i == len(arr)-1:
                break
            temp = i
            while i < len(arr) - 1 and arr[i] < arr[i+1]:
                i += 1
            if i == len(arr)-1:
                break
            if arr[i] == arr[i+1]:
                continue
            while i < len(arr) - 1 and arr[i] > arr[i +1] :
                i += 1
            maxx = max(maxx, i - temp +1)
        return maxx
