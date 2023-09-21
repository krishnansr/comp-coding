# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        tree_paths = []
        stack = [(root, '')]
        while stack:
          node, path = stack.pop()
          updated_path = f"{path}->{str(node.val)}"

          if node.left:
            stack.append((node.left, updated_path))
          if node.right:
            stack.append((node.right, updated_path))
          if not (node.left or node.right):
            tree_paths.append(updated_path[2:])
        return tree_paths