# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA)+1 + len(arrB)+1
    merged_arr = [0] * elements
    # TO-DO
    for i in arrA:
        merged_arr[i] += 1
    for i in arrB:
        merged_arr[i] += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    # print(f'{arr}')
    middle = len(arr)//2
    # print(f'left: {arr[:middle]} right: {arr[middle:]}')
    counter = merge(arr[:middle], arr[middle:])

    position = []

    def rec_counter(index, position, counter):
        if counter[index] != 0:
            arr[len(position)] = index
            counter[index] -= 1
            position.append(1)
        else:
            return 0
        return rec_counter(index, position, counter)

    for i in range(0, len(counter)):
        rec_counter(i, position, counter)
        # first pass
        # while counter[i] != 0:
        #     arr[position] = i
        #     position += 1
        #     counter[i] -= 1

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
