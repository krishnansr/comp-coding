# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        heap_ls = [(lnode.val, i, lnode) for i, lnode in enumerate(lists) if lnode] 
        heapq.heapify(heap_ls)
        
        dummy = _node = ListNode(-1)
        while heap_ls:
            _, i, heap_node = heapq.heappop(heap_ls)
            _node.next = heap_node
            _node = _node.next
            
            if heap_node.next:
                heapq.heappush(heap_ls, (heap_node.next.val, i, heap_node.next))
        
        return dummy.next
    
    def mergeKLists_bruteforce_doesnt_work(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = ListNode()
        _node = dummy
        while any(lists):
            vals = [(i, lnode.val) for i, lnode in enumerate(lists) if lnode is not None]
            i, _ = min(vals, key=lambda x:x[1])
        
            _node.next = lists[i]
            lists[i] = lists[i].next
            _node = _node.next
        
        return dummy.next