class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(flipped_arr, k):
            i , j = 0, k-1
            while i < j :
                flipped_arr[i], flipped_arr[j] = flipped_arr[j], flipped_arr[i]
                i += 1
                j -= 1

        res , n = [], len(arr)
        while n > 0:
            i = arr.index(n)
            if i != n - 1:
                if i != 0: #the number is neither at the beginning nor at its position, so flip it to the beginning
                    res.append(i+1)
                    flip(arr, i+1)
                res.append(n)
                flip(arr, n)  # flip it to the end
            n -= 1
        return res
        
