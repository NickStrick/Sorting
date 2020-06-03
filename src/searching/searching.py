# STRETCH: implement Linear Search
def linear_search(arr, target):

    # if len(arr) == 0:
    #     return -1  # array empty
    # TO-DO: add missing code
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# STRETCH: write an iterative implementation of Binary Search


def binary_search(arr, target):

    if len(arr) == 0:
        return -1  # array empty

    low = 0
    high = len(arr)-1

    # TO-DO: add missing code
    middle = (low+high)//2
    found = 0
    while found == 0:
        if target == arr[middle]:
            found = 1
        elif arr[middle] > target:
            middle = (middle+low)//2
            high = middle
        else:
            middle = (middle+high)//2
            low = middle

    return middle


# STRETCH: write a recursive implementation of Binary Search


def binary_search_recursive(arr, target, low, high):

    middle = (low+high)//2

    if len(arr) == 0:
        return -1  # array empty
    # TO-DO: add missing if/else statements, recursive calls

    # make sure start is low is less then high
    # declare mid
    # if target is less then array[mid] use recursive from low to mid
    # if target is more then array[mid] use recursive from mid to high
    # else mid is equal to target

    if target < arr[middle]:
        return binary_search_recursive(arr, target, low, middle)
    elif target > arr[middle]:
        return binary_search_recursive(arr, target, middle, high)
    else:
        return middle


arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
arr2 = []

print(binary_search_recursive(arr1, -8, 0, len(arr1)-1), 1)
print(binary_search_recursive(arr1, 0, 0, len(arr1)-1), 6)
print(binary_search_recursive(arr2, 6, 0, len(arr1)-1), -1)
print(binary_search_recursive(arr2, 0, 0, len(arr1)-1), -1)
