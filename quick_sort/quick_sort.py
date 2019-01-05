def quick_sort(array):
    # pivot 就是基准值
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        greater = [i for i in array[1:] if i >= pivot]
        less = [i for i in array[1:] if i < pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


