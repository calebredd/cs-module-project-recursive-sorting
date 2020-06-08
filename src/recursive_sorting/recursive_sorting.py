# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = []

    # Your code here
    # Variable for keeping track of first array's index
    i = 0
    # Variable for keeping track of second array's index
    j = 0
    while ( len(merged_arr) < elements ):
        # Check if end of first array has been reached
        if ( i >= len(arrA) ):
            merged_arr.append(arrB[j])
            j+=1
        # Check if end of second array has been reached
        elif ( j >= len(arrB) ):
            merged_arr.append(arrA[i])
            i+=1
        # Compare the two values from each array with eachother
        elif ( arrA[i] > arrB[j] ):
            merged_arr.append(arrB[j])
            j+=1
        # Compare the two values from each array with eachother alternate handling
        else:
            merged_arr.append(arrA[i])
            i+=1
    return merged_arr


# Example array:
# newArr = [4, 1, 3, 5, 7, 0, 9]

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Use Recursion to call the function on each half of the array:
    if len(arr) > 1:
        left = merge_sort(arr[:int(len(arr)/2)])
        right= merge_sort(arr[int(len(arr)/2):])
    # Merge the two halves together in a sorted arrangment by calling the helper function
        arr = merge(left, right)
    return arr


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here
    while start <= mid and mid+1 <= end:
        # If values are already in order move to next index for first half
        if arr[start] < arr[mid+1]:
            start += 1
        else:
        # Grab value and index for smaller value found to prep for the reorder:
            value = arr[mid+1]
            index = mid+1
        # For each index in the list move over to make room:
            while (index != start):
                arr[index] = arr[index-1]
                index -= 1
            arr[start] = value
            # Move markers
            start += 1
            mid += 1

    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here
    if l < r and len(arr):
    # Find the index between left and right indexes:
        a = int((r-l)/2)+l
    # Use Recursion to call the function on each half of the array:
        merge_sort_in_place(arr, l, a)
        merge_sort_in_place(arr, a+1, r)
    #Manipulate current array to sort in place as you go:
        arr = merge_in_place(arr, l, a, r)

    return arr

# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
