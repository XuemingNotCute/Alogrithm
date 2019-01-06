
import search


# 输入名字，检查某人的好友里有无芒果营销商
def test1():
    input = 'you'
    output = search.search(input)
    expected = True
    assert output == expected, output


def test2():
    input = 'thom'
    output = search.search(input)
    expected = False
    assert output == expected, output


def test3():
    input = 'claire'
    output = search.search(input)
    expected = True
    assert output == expected, output

