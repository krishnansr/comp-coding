# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 is None:
            return list2
        elif list2 is None:
            return list1

        if list1.val <= list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next

        _node = head
        while list1 and list2:
            if list1.val <= list2.val:
                _node.next = list1
                list1 = list1.next
            else:
                _node.next = list2
                list2 = list2.next
            _node = _node.next

        _node.next = list1 if list1 else list2
        return head