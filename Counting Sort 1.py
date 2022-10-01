def countingSort(arr):
    output = [0] * 100
    for i in range(len(arr)):
        output[arr[i]] += 1
    return output
    
