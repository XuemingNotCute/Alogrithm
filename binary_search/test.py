import binary_search


def test1():
    # 奇数个列表元素测试
    input = [1, 2, 3, 4, 5, 6, 7]
    output = binary_search.binary_search(input, 6)
    expected = 5
    assert expected == output, output


def test2():
    # 元素不在列表中的测试
    input = [1, 2, 3, 4, 5, 6, 7, 8]
    output = binary_search.binary_search(input, 9)
    expected = None
    assert expected == output, output


def test3():
    # 偶数个列表元素测试
    input = [1, 2, 3, 4, 5, 6, 7, 8]
    output = binary_search.binary_search(input, 6)
    expected = 5
    assert expected == output, output
