# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # find the next smallest element
        # (hint, cna do in 3 lines of code)
        for j in range(cur_index +1, len(arr)):
            # compare all these values to the vlaue at cur_index
            # find the smallest
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr



# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    

for i in range(0, )
    j = i+1

    if arr[i] > arr[j]:
        arr[i], arr[j] = arr[j], arr[i]
        made_a_swap = True
    


# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    if len(arr) == 0:
        return arr

    counts = [0] * (maximum +1)

    for value in arr:
        counts[value] += 1

    j = 0
    for i in range(len(count)):
        while count[i] > 0:
            arr[j] = i
            j += 1
            count[i] -= 1

    return arr
