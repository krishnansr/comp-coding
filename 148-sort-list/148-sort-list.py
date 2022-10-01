# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # solution fron : https://leetcode.com/problems/merge-two-sorted-lists/
        
        dummy = ListNode(val=float('-inf'), next=list1)  # makeshift dummy node to keep track of head
        _node = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                _node.next = list1
                list1 = list1.next
            else:
                _node.next = list2
                list2 = list2.next
            _node = _node.next

        _node.next = list1 if list1 else list2  # append leftover elements after traversal
        return dummy.next     

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        slow.next, head2 = None, slow.next  # split the lists into two
        left_sorted = self.sortList(head)
        right_sorted = self.sortList(head2)
        head = self.mergeTwoLists(left_sorted, right_sorted)
        return head