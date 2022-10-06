class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        window = sum(arr[:k-1])
        counter = 0
        for i in range(k-1, len(arr)):
            window += arr[i]
            if window / k >= threshold: 
                counter += 1
            window -= arr[i - (k - 1)]
        return counter
    ########################################
        # This can alsow works , but amizingly it failed at 68/69 test cases with array size of 100,000 ):
        i = counter = 0
        j = k
        while j <= len(arr):
            window = arr[i:j]
            if sum(window) / k >= threshold:
                counter += 1
            i += 1
            j += 1
        return counter
        
