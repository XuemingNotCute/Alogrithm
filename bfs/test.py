
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

    
# 但是这个测试有一个问题。只测了从a->b有没有路径，没有测是不是最短路径。
def test3():
    input = 'claire'
    output = search.search(input)
    expected = True
    assert output == expected, output

