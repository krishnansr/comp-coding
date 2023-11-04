# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # O(n) time, O(log(n)) space if balances BST
        # this solution leverages that the input is BST not just BT, so in-order traversal of BST is a sorted array. And in a sorted array, you can search iteratively
        # Solution from https://leetcode.com/problems/two-sum-iv-input-is-a-bst/discuss/1420711/C++JavaPython-3-solutions:-HashSet-Stack-Python-yield-Solutions-O(H)-space
        
        def in_order_traversal(node):
            # returns sorted array in ascending order
            if node:
                yield from in_order_traversal(node.left)
                yield node.val
                yield from in_order_traversal(node.right)

        def in_order_traversal_rev(node):
            # returns sorted array in descending order
            if node:
                yield from in_order_traversal_rev(node.right)
                yield node.val
                yield from in_order_traversal_rev(node.left)

        left_gen = in_order_traversal(root)
        right_gen = in_order_traversal_rev(root)

        left = next(left_gen)
        right = next(right_gen)
        while left < right:
            if left + right == k:
                return True
            elif left + right < k:
                left = next(left_gen)
            else:
                right = next(right_gen)
        return False
    
    
    def findTarget_bt(self, root: Optional[TreeNode], k: int) -> bool:
        # O(n) time, O(n) space
        # this solution doesn't leverage the fact that it is a binary search tree
        # just uses it as a binary tree and iterates through it like two-sum
        if root is None:
            return False
        
        subtrahend_set = set()
        queue = [root]
        while queue:
            node = queue.pop(0)  # BFS
            
            if k - node.val in subtrahend_set:
                return True
            subtrahend_set.add(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        return False