from collections import deque


# 这个算法的背景是检查人际网络的有向图里面，某人的好友里有无芒果营销商。要点一, 用散列表表示图
def return_dict(name):
    graph = dict()
    graph['you'] = ['bob', 'alice', 'claire']
    graph['bob'] = ['anuj', 'peggy']
    graph['alice'] = ['peggy']
    graph['claire'] = ['thom', 'jonny']
    graph['anuj'] = []
    graph['peggy'] = []
    graph['thom'] = []
    graph['jonny'] = []
    return graph[name]


def person_is_seller(name):
    return name[-1] == 'm'


def search(name):
    # 要点二, 用队列实现 bfs
    search_queue = deque()
    search_queue.extend(return_dict(name))
    # searched 是记录了已经被检查过的元素，这样防止重复检查，避免死循环危险
    searched = []
    while search_queue:
        person = search_queue.popleft()
        # 检查重复
        if person not in searched:
            if person_is_seller(person):
                print(person + ' is a mango seller!')
                return True
            else:
                searched.append(person)
                search_queue.extend(return_dict(person))
    return False

