# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def helper(node):
            if not node: return
            if node.left and node.right:
                tmp_node = node.left
                node.left = node.right
                node.right = tmp_node
            elif node.left:
                tmp_node = node.left
                node.left = None
                node.right = tmp_node
            elif node.right:
                tmp_node = node.right
                node.right = None
                node.left = tmp_node

            helper(node.left)
            helper(node.right)

        helper(root)
        return root
        