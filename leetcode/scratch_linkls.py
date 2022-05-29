from typing import *
from functools import lru_cache
from itertools import repeat
from math import *
from collections import OrderedDict

class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __repr__(self):
        return self.data.__repr__()


class LinkedList:
    def __init__(self, dataset=None):
        self.head = None
        self.size = 0

        if dataset is not None:
            _node = Node(dataset.pop(0))
            self.head = _node  # handle head node separately as you need to keep track of it
            self.size += 1
            for elem in dataset:
                _node.next = Node(elem)
                _node = _node.next
                self.size += 1

    def __iter__(self):
        _node = self.head
        while _node is not None:
            yield _node
            _node = _node.next

    def __repr__(self):
        return ' -> '.join(map(str, self.__iter__()))

    def length(self):
        count = 0
        for _node in self.__iter__():
            count += 1
        return count

    def append(self, data):
        pass

    def appendleft(self, data):
        _node = Node(data=data, next=self.head)
        self.head = _node

    def extend(self, dataset):
        pass

    def insert(self):
        pass

    def pop(self):
        pass

    def popleft(self, node):
        pass

    def remove(self):
        pass


class Solution:
    def fn(self):
        pass


if __name__ == '__main__':
    s = Solution()
    # print(s.construct2DArray(original = [1,1,1,1], m = 1, n = 4))

    ls = LinkedList([1, 2, 3, 4])
    print(ls)

    ls.appendleft(0)
    print(ls)

    ls.append(99)
    print(ls)


    print()