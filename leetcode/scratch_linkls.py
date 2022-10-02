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

ListNode = Node

class LinkedList:
    def __init__(self, dataset=None):
        self.head = None
        self.tail = None  # todo: extra space - can use this to append at O(1) time, need to update suitable like head
        self.size = 0  # todo: can use this to get length in const. time, need to update as suitable

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

    def reverse(self):
        prev = None
        _node = self.head
        while _node is not None:
            temp_next = _node.next
            _node.next = prev
            prev = _node
            _node = temp_next
        self.head = prev  # don't forget to update head

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0


class Solution:
    def middleNode(self, head: Optional[Node]) -> Optional[Node]:
        fast_node = head
        slow_node = head
        while fast_node and fast_node.next:
            slow_node = slow_node.next
            fast_node = fast_node.next.next
        return slow_node

    def isPalindrome(self, head: Optional[Node]) -> bool:
        # get middle node
        fast_node = middle = head
        while fast_node and fast_node.next:
            middle = middle.next
            fast_node = fast_node.next.next

        # reverse second half of linked list
        tail = middle
        _node = middle.next
        while _node is not None:
            temp_next = _node.next
            _node.next = tail
            tail = _node
            _node = temp_next

        # compare from both ends for palindrome check
        while head != tail and head != middle:
            if head.data != tail.data:
                return False
            head = head.next
            tail = tail.next

        return True

    def removeElements(self, head: Optional[Node], val: int) -> Optional[Node]:
        prev_node = None
        _node = head
        while _node is not None:
            if _node.data == val:
                if _node == head:  # handle head separately
                    head = _node.next
                else:
                    prev_node.next = _node.next
            else:
                prev_node = _node  # update previous node only when no nodes are deleted
            _node = _node.next
        return head

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        prev = head
        _node = head.next
        while _node:
            if prev.data == _node.data:
                prev.next = _node.next
            else:
                prev = _node
            _node = _node.next

        return head

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(data=float('-inf'), next=list1)  # makeshift dummy node to keep track of head
        _node = dummy
        while list1 and list2:
            if list1.data <= list2.data:
                _node.next = list1
                list1 = list1.next
            else:
                _node.next = list2
                list2 = list2.next
            _node = _node.next

        _node.next = list1 if list1 else list2  # append leftover elements after traversal
        return dummy.next

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1, next=head)
        left = dummy
        right = head

        while n:  # move the right pointer to desired start position
            right = right.next
            n -= 1
        while right:  # iterate till left reaches len - n position
            right = right.next
            left = left.next

        left.next = left.next.next  # node deletion
        return dummy.next

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1, next=head)
        _node = dummy
        while _node.next and _node.next.next:
            temp_next = _node.next
            _node.next = _node.next.next  # bring back 2

            temp_next.next = _node.next.next
            _node.next.next = temp_next  # move forward 1

            _node = _node.next.next  # iterate for nex pair

        return dummy.next


if __name__ == '__main__':
    s = Solution()
    # print(s.construct2DArray(original = [1,1,1,1], m = 1, n = 4))

    ls1 = LinkedList([1, 2, 3, 4])
    # ls.extend([0, 0, 0, 1, 2, 2, 3, 3, 4, 5, 6, 6, 6])
    res = s.swapPairs(ls1.head)
    ls1.head = res
    print(ls1)

    """
    ls.extend([1, 2, 3, 4])
    print(ls)
    ls.appendleft(0)
    print(ls)

    print(ls.popleft())
    print(ls)

    ls.append(99)
    print(ls)

    print(ls.pop())
    print(ls)

    print(ls.index(1))

    print(ls)
    print(ls.length())
    """
