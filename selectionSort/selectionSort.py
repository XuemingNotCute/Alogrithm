def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(0, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    new_arr = []
    for i in range(0, len(arr)):
        smallest_index = find_smallest(arr)
        smallest = arr.pop(smallest_index)
        new_arr.append(smallest)
    return new_arr
