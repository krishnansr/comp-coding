# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def in_order_traversal(node):
            # returns sorted array in ascending order.
            if node:
                yield from in_order_traversal(node.left)
                yield node.val
                yield from in_order_traversal(node.right)

        for val in in_order_traversal(root):
            if k == 1:
                return val
            k -= 1
        return -1

    def kthSmallest_iterative(self, root: Optional[TreeNode], k: int) -> int:
        # Idea since it's a BST, in-order traversal gives the sorted array.
        # Stop the in-order traversal at the kth iteration to get kth smallest element.

        node = root
        stack = []
        while node or stack:
            # Reach the left most Node of the current Node
            while node:
                stack.append(node)
                node = node.left
            
            # BackTrack from the empty subtree and visit the Node
            # at the top of the stack
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val

            # We have visited the node and its left 
            # subtree. Now, it's right subtree's turn
            node = node.right 

        return -1