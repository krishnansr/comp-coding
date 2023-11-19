# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # inorder traversal must be sorted - iterative approach.
        prev_val = float('-inf')

        node = root
        stack = []
        while stack or node:
            # Reach the left most Node of the current Node.
            while node:
                stack.append(node)
                node = node.left

            # BackTrack from the empty subtree and visit the Node at the top of the stack.
            node = stack.pop()
            if node.val <= prev_val:
                return False
            prev_val = node.val
            
            # We have visited the node and its left subtree. Now, it's right subtree's turn
            node = node.right
        return True
    
    def isValidBST_recursive(self, root: Optional[TreeNode]) -> bool:
        # inorder traversal must be sorted.
        def inorder_traversal(node):
            if node:
                yield from inorder_traversal(node.left)
                yield node.val
                yield from inorder_traversal(node.right)
        
        prev_val = float('-inf')
        for val in inorder_traversal(root):
            if val <= prev_val:
                return False
            prev_val = val
        return True
    
    def isValidBST_DFS(self, root):
        def dfs(node, floor, ceiling):
            if not node: 
                return True
            if node.val <= floor or node.val >= ceiling:
                return False
            
            # root is max val in left tree; and is the min_val in the right tree
            return dfs(node.left, floor=floor, ceiling=node.val) and dfs(node.right, floor=node.val, ceiling=ceiling)
    
        return dfs(root, floor=float('-inf'), ceiling=float('inf'))
