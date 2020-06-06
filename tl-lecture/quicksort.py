
def partition(arr):
    left = []
    right = []  
    pivot = arr[0]

    # iterate over the rest of the array
    for num in arr[1:]:
        # if element is greater thean pivot in the right
        if num > pivot:right.append(num)
        # else , in the left
        else: left.append(num)

    return left,pivot, right


def quick_sort(arr):

    if len(arr) == 0:
        return arr

    # partition here into left, pivot, and right
    # divide!
    left, pivot, right = partition(arr)

    return quick_sort(left) + pivot + quick_sort(right)

    
