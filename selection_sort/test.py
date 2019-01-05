import selection_sort


def test1():
    input = [5, 8, 9, 0, 3, 5, 2, 1]
    output = selectionSort.selection_sort(input)
    expected = [0, 1, 2, 3, 5, 5, 8, 9]
    assert output == expected, output


def test2():
    input = [100, 8, 9, 50, 45, 34, 12, 7, 1000]
    output = selectionSort.selection_sort(input)
    expected = [7, 8, 9, 12, 34, 45, 50, 100, 1000]
    assert output == expected, output


def test3():
    input = [5, 3, 6, 2, 10]
    output = selectionSort.selection_sort(input)
    expected = [2, 3, 5, 6, 10]
    assert output == expected, output
