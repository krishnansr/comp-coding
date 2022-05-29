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

        if dataset is not None:
            _node = Node(dataset.pop(0))
            self.head = _node  # handle head node separately as you need to keep track of it
            for elem in dataset:
                _node.next = Node(elem)
                _node = _node.next

    def __iter__(self):
        # makes your life a lot easier with this list traversal subroutine
        _node = self.head
        while _node is not None:
            yield _node
            _node = _node.next

    def __repr__(self):
        return 'ls: ' + ' -> '.join(map(str, self))

    def length(self):
        # redundant: can instead keep track on every addition/deletion
        count = 0
        for _node in self:
            count += 1
        return count

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        for _node in self:
            pass
        _node.next = Node(data)

    def appendleft(self, data):
        _node = Node(data=data, next=self.head)
        self.head = _node

    def extend(self, dataset):
        if self.head is None:
            last_node = Node(dataset.pop(0))
            self.head = last_node
        else:
            for last_node in self:
                pass

        for elem in dataset:
            last_node.next = Node(elem)
            last_node = last_node.next

    def insert(self, index, data):
        if index == 0:
            self.appendleft(data)
            return

        for i, _node in enumerate(self):
            if i + 1 == index:
                new_node = Node(data=data, next=_node.next)
                _node.next = new_node
                return
        raise Exception(f"Invalid insert index specified for list")

    def pop(self):
        if self.head is None or self.head.next is None:
            # handle lists of size 0 & 1
            self.head = None
            return

        for _node in self:
            if _node.next.next is None:
                _node.next = None
                return

    def popleft(self):
        if self.head is None:
            return
        self.head = self.head.next

    def remove_data(self, data):
        if self.head is None:
            raise Exception("Trying to remove data from empty list")

        if self.head.data == data:
            self.head = self.head.next
            return

        prev_node = self.head
        for _node in self:
            if _node.data == data:
                prev_node.next = _node.next
                return
            prev_node = _node
        raise Exception(f"No node with data {data} found")

    def remove_index(self, index):
        if self.head is None:
            raise IndexError("Trying to remove data from empty list")

        if index == 0:
            self.head = self.head.next

        prev_node = self.head
        for i, _node in enumerate(self):
            if i == index:
                prev_node.next = _node.next
                return
            prev_node = _node
        raise IndexError(f"Trying to remove index {index} that is out of bounds")

    def index(self, index):
        for i, _node in enumerate(self):
            if i == index:
                return _node
        raise IndexError(f"Invalid index {index}")


class Solution:
    def fn(self):
        pass


if __name__ == '__main__':
    s = Solution()
    # print(s.construct2DArray(original = [1,1,1,1], m = 1, n = 4))

    ls = LinkedList()

    ls.extend([1, 2, 3, 4])
    print(ls)
    """
    ls.appendleft(0)
    print(ls)

    print(ls.popleft())
    print(ls)

    ls.append(99)
    print(ls)

    print(ls.pop())
    print(ls)

    print(ls.index(1))
    """

    ls.insert(0, 77)
    print(ls)
    print(ls.length())