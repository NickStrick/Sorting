def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    
    return -1 # not found


def binary_search(arr, target):

    if len(arr) == 0:
        return -1 

    low = 0
    high = len(arr)-1

    while low <= high:
        middle = (low + high)//2
        if arr[middle] == target:
            return middle

        if target < arr[middle]:
            high = middle - 1
        else:
            
        