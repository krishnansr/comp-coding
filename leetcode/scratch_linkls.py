from typing import *
from functools import lru_cache
from itertools import repeat
from math import *
from collections import OrderedDict

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:

    def count_nodes(self, head):
        count = 1
        while head.next is not None:
            count += 1
            head = head.next
        return count

    def delete_node(self, node):
        pass

class Solution:
    def fn(self):
        pass

if __name__ == '__main__':
    s = Solution()
    # print(s.construct2DArray(original = [1,1,1,1], m = 1, n = 4))

