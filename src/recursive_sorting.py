# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    # second pass
    # for i in arrA:
    #     merged_arr[i] += 1
    # for i in arrB:
    #     merged_arr[i] += 1

    # third pass
    first = 0
    second = 0
    for index in range(0, elements):
        if first >= len(arrA):
            merged_arr[index] = arrB[second]
            second += 1
        elif second >= len(arrB):
            merged_arr[index] = arrA[first]
            first += 1
        elif arrA[first] < arrB[second]:
            merged_arr[index] = arrA[first]
            first += 1
        else:
            merged_arr[index] = arrB[second]
            second += 1
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    # second pass
    # middle = len(arr)//2
    # counter = merge(arr[:middle], arr[middle:])
    # position = []
    # def rec_counter(index, position, counter):
    #     if counter[index] != 0:
    #         arr[len(position)] = index
    #         counter[index] -= 1
    #         position.append(1)
    #     else:
    #         return 0
    #     return rec_counter(index, position, counter)
    # for i in range(0, len(counter)):
    #     rec_counter(i, position, counter)

    # third pass
    if len(arr) > 1:
        left = merge_sort(arr[0: len(arr) // 2])
        right = merge_sort(arr[len(arr) // 2:])
        arr = merge(left, right)

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO
    begin = mid + 1

    if arr[mid] <= arr[begin]:
        return

    while start <= mid and begin <= end:
        if arr[start] <= arr[begin]:
            start += 1
        else:
            value = arr[begin]
            index = begin
            while index != start:
                arr[index] = arr[index - 1]
                index -= 1
            arr[start] = value
            start += 1
            mid += 1
            begin += 1

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO
    if l < r:
        m = l + (r - l) // 2
        merge_sort_in_place(arr, l, m)
        merge_sort_in_place(arr, m + 1, r)

        merge_in_place(arr, l, m, r)

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
